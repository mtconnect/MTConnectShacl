$: << './vocab'

require 'rdf'
require 'rdf/vocab'
require 'rdf/rdfxml'
require 'rdf/turtle'

include RDF

module MTConnect
  Device = Class.new(RDF::StrictVocabulary("https://purl.mtconnect.org/ontology/")) do
    ontology :"https://purl.mtconnect.org/ontology/",
      label: {"en-us": "MTConnect Ontology"},
      type: "http://www.w3.org/2002/07/owl#Ontology"

    term :Component,
         label: {"en-us": "component"},
         type: "http://www.w3.org/2002/07/owl#Class"

    term :DataItem,
         label: {'en-us': 'data item'},
         type: "http://www.w3.org/2002/07/owl#Class"


    property :hasComponent,
             label: {'en-us': 'has component'},
             type: [RDF::OWL.ObjectProperty, RDF::OWL.TransitiveProperty],
             domain: self.Component,
             range: self.Component

    property :componentOf,
             label: {'en-us': 'has component'},
             type: [RDF::OWL.ObjectProperty],
             inverseOf: self.hasComponent,
             domain: self.Component,
             range: self.Component

    property :observes,
          label: {'en-us': 'observes'},
          type: [RDF::OWL.ObjectProperty],
          domain: self.Component,
          range: self.DataItem

    property :hasName,
             label: {'en-us': 'has name'},
             type: [RDF::OWL.DatatypeProperty],
             range: RDF::XSD.string

    property :hasIdentifier,
             label: {'en-us': 'has identifier'},
             type: [RDF::OWL.DatatypeProperty],
             range: RDF::XSD.string

    property :hasUnits,
             label: {'en-us': 'has units'},
             type: [RDF::OWL.DatatypeProperty],
             range: RDF::XSD.string


    property :observedBy,
          label: {'en-us': 'observed by'},
          type: [RDF::OWL.ObjectProperty],
          inverseOf: self.observes

    term :Device,
         label: {"en-us": "machine"},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"
    
    term :Axis,
         label: {"en-us": "axis"},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"
               
    term :Axes,
         label: {"en-us": "axes"},
         subClassOf: [self.Component,
               term(onProperty: self.hasComponent,
                    someValuesFrom: self.Axis,
                    type: "http://www.w3.org/2002/07/owl#Restriction")],
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Linear,
         label: {"en-us": "linear motion system"},
         subClassOf: self.Axis,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Rotary,
         label: {"en-us": "rotary motion system"},
         subClassOf: self.Axis,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Controller,
         label: {"en-us": "controller"},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"
    
    term :Path,
         label: {"en-us": "control system path"},
         subClassOf: self.Controller,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Motor, 
         label: {"en-us": "motor"},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Ballscrew, 
         label: {"en-us": "ballscrew"},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"
     
     term :Systems,
         label: {"en-us": "systems"},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

     term :System,
         label: {"en-us": "system"},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Door, 
         label: {"en-us": "door"},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :ElectricalSystem, 
         label: {"en-us": "electrical system"},
         subClassOf: self.System,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :HydraulicSystem, 
         label: {"en-us": "hydraulic system"},
         subClassOf: self.System,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :PneumaticSystem, 
         label: {"en-us": "pneumatic system"},
         subClassOf: self.System,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :LubricationSystem, 
         label: {"en-us": "lubrication system"},
         subClassOf: self.System,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Stock, 
         label: {"en-us": "stock"},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :PartOccurrence, 
         label: {"en-us": "part"},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Enclosure,
         label: {'en-us': 'enclosure'},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Structure,
         label: {'en-us': 'enclosure'},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

     term :Link,
          label: {'en-us': 'link'},
          subClassOf: self.Structure,
          type: "http://www.w3.org/2002/07/owl#Class"

    term :Structures,
         label: {'en-us': 'structure'},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Room,
         label: {'en-us': 'room'},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Sensor,
         label: {'en-us': 'sensor'},
         subClassOf: self.Component,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Event,
          label: {'en-us': 'event'},
          subClassOf: self.DataItem,
          type: "http://www.w3.org/2002/07/owl#Class"
    
    term :Sample,
          label: {'en-us': 'sample'},
          subClassOf: self.DataItem,
          type: "http://www.w3.org/2002/07/owl#Class"

    term :Condition,
        label: {'en-us': 'condition'},
        subClassOf: self.DataItem,
        type: "http://www.w3.org/2002/07/owl#Class"

    term :Position,
         label: {'en-us': 'position'},
         subClassOf: self.Sample,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :PathPosition,
         label: {'en-us': 'path position'},
         subClassOf: self.Sample,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :ControllerMode,
         label: {'en-us': 'controller mode'},
         subClassOf: self.Event,
         type: "http://www.w3.org/2002/07/owl#Class"

    term :Execution,
         label: {'en-us': 'execution'},
         subClassOf: self.Event,
         type: "http://www.w3.org/2002/07/owl#Class"

  end

end

module Inst
  Data = Class.new(RDF::Vocabulary("http://example.com/data/")) do
    ontology :"http://example.com/data/",
      label: {"en-us": "Machine Ontology"},
      type: "http://www.w3.org/2002/07/owl#Ontology"
  end
end

Prefixes = {
  mt: MTConnect::Device.to_uri,
  data: Inst::Data.to_uri,
  rdfs: RDF::RDFS.to_uri,
  rdfv: RDF::RDFV.to_uri,
  owl: RDF::OWL.to_uri,
  xs: RDF::XSD.to_uri
}

Colors = {
  obo: "DFA702",
  core: "1E90FF",
  qp: "1E90FF",
  av: "1E90FF",
  ex: "Green",
  data: "76608A"
}

if __FILE__ == $0
  onto = RDF::Graph.new
  onto << MTConnect::Device.to_enum
    
  RDF::Writer.open("mtconnect.ttl", prefixes: Prefixes) do |w|
    w << onto
  end
end
