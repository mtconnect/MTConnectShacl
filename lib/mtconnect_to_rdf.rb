require 'rexml/document'
require 'time'
require 'rdf'
require 'rdf/vocab'
require 'mtconnect'
require 'rdf/rdfxml'
require 'rdf/turtle'

# The class that converts the MTConnect information model to an IOF compatible
# ontology.

class MTConnectToRDF
  attr_reader :graph

  def is_subclass_of(cls, base)
    !cls.entail(:subClassOf).find { |t| t == base }.nil?
  end

  # Parse the XML to find the components and create a graph of individuals
  def initialize(xml)
    @doc = REXML::Document.new(xml)

    @graph = RDF::Graph.new
    @graph << Inst::Data.to_enum

    RDF::Reasoner.apply(:rdfs, :owl)
    
    @doc.each_element('//Device') do |dev|
      @device_name = dev[:name]
      add_component(dev)
    end
  end

  # Create a sub-entity IRI
  def sub_iri(names, ext)
    sub = (names + Array(ext)).join('-')
    Inst::Data[sub]
  end

  # Add an instance of a type to the parent using a relation
  def add_instance(iri, name, relation, type)
    @graph << (s = Statement.new(name, RDF.type, type))
    @graph << [iri, relation, s.subject]
    s
  end

  # Recursively add components
  def add_component(comp, names = [], level = 0)
    type = (comp[:type] || comp.name).to_sym
    puts "#{'  ' * level}#{comp.name} #{comp[:id]} #{type.inspect}"
    cls = MTConnect::Device[type] if MTConnect::Device.methods.include?(type)
    
    if cls
      parent = Inst::Data[names.join('-')] unless names.empty?
      names = names.dup << "#{comp[:uuid] || comp[:id]}"
      iri = Inst::Data[names.join('-')]

      @graph << [iri, RDF.type, cls]      
      @graph << [parent, MTConnect::Device.hasComponent, iri] if parent
      @graph << [iri, MTConnect::Device.hasName, comp[:name]] if comp[:name]
      @graph << [iri, MTConnect::Device.hasIdentifier, comp[:uuid] || comp[:id]]
      
      comp.each_element('./DataItems/DataItem') do |di|
        di_type = di[:type].split("_").map(&:capitalize).join.to_sym

        if di[:category] != 'CONDITION' and MTConnect::Device.methods.include?(di_type)
          dicls = MTConnect::Device[di_type]
          puts "#{'  ' * (level + 1)}** #{di[:category]} #{di_type} #{di[:subType]} #{di[:units]}"

          di_inst = sub_iri(names, di_type.to_s)
          @graph << [di_inst, RDF.type, dicls]
          @graph << [iri, MTConnect::Device.observes, di_inst]
          @graph << [di_inst, MTConnect::Device.hasName, di[:name]] if di[:name]
          @graph << [di_inst, MTConnect::Device.hasIdentifier, di[:id]]
        end
      end      
    end

    # Recurse each composition
    #comp.each_element("./Compositions/*") do |cmp|
    #  add_component(cmp, names, level + 1)
    #end

    # Recurse each components
    comp.each_element('./Components/*') do |child|
      add_component(child, names, level + 1)
    end
  end

  def generate(machine)
    # Write out the individuals for the machine in rdfxml and turtle formats
    debug = Logger.new($stderr)
    debug.level = Logger::DEBUG
    debug.formatter = lambda {|severity, datetime, progname, msg| "#{severity} #{msg}\n"}
    @graph << MTConnect::Device.to_enum
    RDF::Writer.open("#{machine}.ttl", prefixes: Prefixes) do |w|
      w << @graph
    end
  end
end
