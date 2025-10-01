import owlready2 as owl
import os
import re

if os.path.exists("mtconnect.rdf"):
    os.remove("mtconnect.rdf")

MTConnect = owl.get_ontology("https://purl.mtconnect.org/ontology/")
MTConnect.label = [owl.locstr("Machine Ontology", "en")]
MTConnect.base_iri = "https://purl.mtconnect.org/ontology/"

with MTConnect:
  # Data types
  class hasName(owl.DataProperty):
    """A property indicating the name of a component."""
    label = owl.locstr("has name", "en")
    domain = [owl.Thing]
    range = [str]
  
  class hasId(owl.DataProperty):
    """A property indicating the ID of a component."""
    label = owl.locstr("has id", "en")
    domain = [owl.Thing]
    range = [str]
    
  class hasUUID(owl.DataProperty):
    """A property indicating the UUID of a component."""
    label = owl.locstr("has uuid", "en")
    domain = [owl.Thing]
    range = [str]
  
  # Data Items/Observables
  class DataItem(owl.Thing):
    """An observable in the MTConnect ontology."""
    label = owl.locstr("Observable", "en")
    is_a = [hasId.some(str), hasName.some(str)]
    
  class EventDataItem(DataItem):
    """An event in the MTConnect ontology."""
    label = owl.locstr("Event", "en")
    
  class SampleDataItem(DataItem):
    """A sample in the MTConnect ontology."""
    label = owl.locstr("Sample", "en")

  class ConditionDataItem(DataItem):
    """A condition in the MTConnect ontology."""
    label = owl.locstr("Condition", "en")
    
  # Some Sample Data Item types
  class PositionDataItem(SampleDataItem):
    """A position observable in the MTConnect ontology."""
    label = owl.locstr("Position", "en")
    
  class PositionActualDataItem(PositionDataItem):
    """An actual position observable in the MTConnect ontology."""
    label = owl.locstr("Position Actual", "en")
    
  class PositionCommandedDataItem(PositionDataItem):
    """A commanded position observable in the MTConnect ontology."""
    label = owl.locstr("Position Commanded", "en")

  class AngleDataItem(SampleDataItem):
    """An angle observable in the MTConnect ontology."""
    label = owl.locstr("Angle", "en")
    
  class AngleActualDataItem(AngleDataItem):
    """An actual angle observable in the MTConnect ontology."""
    label = owl.locstr("Angle Actual", "en")
    
  class AngleCommandedDataItem(AngleDataItem):
    """A commanded angle observable in the MTConnect ontology."""
    label = owl.locstr("Angle Commanded", "en")
    
  class PathFeedrateDataItem(SampleDataItem):
    """A path feedrate observable in the MTConnect ontology."""
    label = owl.locstr("Path Feedrate", "en")
    
  class PathFeedrateActualDataItem(PathFeedrateDataItem):
    """An actual path feedrate observable in the MTConnect ontology."""
    label = owl.locstr("Path Feedrate Actual", "en")
    
  class PathFeedrateCommandedDataItem(PathFeedrateDataItem):
    """A commanded path feedrate observable in the MTConnect ontology."""
    label = owl.locstr("Path Feedrate Commanded", "en")
    
  class PathPositionDataItem(SampleDataItem):
    """A path position observable in the MTConnect ontology."""
    label = owl.locstr("Path Position", "en")
    
  class LoadDataItem(SampleDataItem):
    """A load observable in the MTConnect ontology."""
    label = owl.locstr("Load", "en")
  
  class TemperatureDataItem(SampleDataItem):
    """A temperature observable in the MTConnect ontology."""
    label = owl.locstr("Temperature", "en")
    
  class AngularVelocitDataItem(SampleDataItem):
    """An angular velocity observable in the MTConnect ontology."""
    label = owl.locstr("Angular Velocity", "en")
    
  class RotaryVelocityDataItem(SampleDataItem):
    """A rotary velocity observable in the MTConnect ontology."""
    label = owl.locstr("Rotary Velocity", "en")
    
  class RotaryVelocityActualDataItem(RotaryVelocityDataItem):
    """An actual rotary velocity observable in the MTConnect ontology."""
    label = owl.locstr("Rotary Velocity Actual", "en")
    
  class RotaryVelocityCommandedDataItem(RotaryVelocityDataItem):
    """A commanded rotary velocity observable in the MTConnect ontology."""
    label = owl.locstr("Rotary Velocity Commanded", "en")
    
  class PathFeedrateOverrideDataItem(SampleDataItem):
    """A path feedrate override observable in the MTConnect ontology."""
    label = owl.locstr("Path Feedrate Override", "en")
    
  class PathFeedrateOverrideRapidDataItem(PathFeedrateOverrideDataItem):
    """A path feedrate override rapid observable in the MTConnect ontology."""
    label = owl.locstr("Path Feedrate Override Rapid", "en")
    
  class PathFeedrateOverrideProgrammedDataItem(PathFeedrateOverrideDataItem):
    """A path feedrate override programmed observable in the MTConnect ontology."""
    label = owl.locstr("Path Feedrate Override Programmed", "en")
    
  # Some event types
  class AvailabilityDataItem(EventDataItem):
    """An availability event in the MTConnect ontology."""
    label = owl.locstr("Availability", "en")  
    
  class AssetChangedDataItem(EventDataItem):
    """An asset changed event in the MTConnect ontology."""
    label = owl.locstr("Asset Changed", "en")
    
  class AssetRemovedDataItem(EventDataItem):
    """An asset removed event in the MTConnect ontology."""
    label = owl.locstr("Asset Removed", "en")
    
  class AssetAddedDataItem(EventDataItem):
    """An asset added event in the MTConnect ontology."""
    label = owl.locstr("Asset Added", "en")
    
  class ExecutionDataItem(EventDataItem):
    """An execution event in the MTConnect ontology."""
    label = owl.locstr("Execution", "en")
    
  class ControllerMode(EventDataItem):
    """A controller mode event in the MTConnect ontology."""
    label = owl.locstr("Controller Mode", "en")
    
  class AxisStateDataItem(EventDataItem):
    """An axis state event in the MTConnect ontology."""
    label = owl.locstr("Axis State", "en")        
        
  class LineNumberDataItem(EventDataItem):
    """A line number observable in the MTConnect ontology."""
    label = owl.locstr("Line Number", "en")
    
  class LineLabelDataItem(EventDataItem):
    """A line label observable in the MTConnect ontology."""
    label = owl.locstr("Line Label", "en")
    
  class MaterialDataItem(EventDataItem):
    """A material event in the MTConnect ontology."""
    label = owl.locstr("Material", "en")
    
  class UserDataItem(EventDataItem):
    """A user event in the MTConnect ontology."""
    label = owl.locstr("User", "en")

  # Some condition types      
  class SystemConditionDataItem(ConditionDataItem):
    """A system condition in the MTConnect ontology."""
    label = owl.locstr("System Condition", "en")
    
  class TemperatureConditionDataItem(ConditionDataItem):
    """A temperature condition in the MTConnect ontology."""
    label = owl.locstr("Temperature Condition", "en")

  class PositionConditionDataItem(ConditionDataItem):
    """A position condition in the MTConnect ontology."""
    label = owl.locstr("Position Condition", "en")

  # Assets
  class Asset(owl.Thing):
    """An asset in the MTConnect ontology."""
    label = owl.locstr("Asset", "en")

  # Base MTConnect Ontology
  class Component(owl.Thing):
    """A component in the MTConnect ontology."""
    label = owl.locstr("Component", "en")
    is_a = [hasId.some(str), hasName.some(str), hasUUID.some(str)]

  class Capability(owl.Thing):
    """A capability in the MTConnect ontology."""
    label = owl.locstr("Capability", "en")

  class hasCapability(Component >> Capability):
    """A property indicating that a component has a capability."""
    label = owl.locstr("has capability", "en")

  class isCapabilityOf(owl.ObjectProperty):
    """A property indicating that a capability is part of a component."""
    label = owl.locstr("is capability of", "en")    
    inverse_property = hasCapability

  class observes(Component >> DataItem):
    """A property indicating that a component observes a data item."""
    label = owl.locstr("observes", "en")

    # Some properties for base model
  class hasComponent(Component >> Component):
    """A property indicating that a component has another component."""
    label = owl.locstr("has component", "en")

  Component.is_a.append(hasComponent.some(Component)) 
  Component.is_a.append(observes.some(DataItem))
  Component.is_a.append(hasCapability.some(Capability))
  
  class observedBy(owl.ObjectProperty):
    """A property indicating that a data item is observed by a component."""
    label = owl.locstr("observed by", "en")    
    inverse_property = observes
    
  class isComponentOf(owl.ObjectProperty):
    """A property indicating that a component is part of another component."""
    label = owl.locstr("is component of", "en")    
    inverse_property = hasComponent

  class hasReference(Component >> Component):
    """A property indicating that a component has a reference to another component."""
    label = owl.locstr("has reference", "en")
    
  class referenceOf(owl.ObjectProperty):
    """A property indicating that a component is referenced by another component."""
    label = owl.locstr("reference of", "en")    
    inverse_property = hasReference

  class Device(Component):
    """A device in the MTConnect ontology."""
    label = owl.locstr("Device", "en")
    subclass_of = [observes.some(AvailabilityDataItem)]
    
  class hasAssetCount(owl.DataProperty):
    """A property indicating the asset count of a device."""
    label = owl.locstr("has asset count", "en")
    domain = [Device]
    range = [int]
  
  class hasAssetBufferSize(owl.DataProperty):
    """A property indicating the buffer size of a device."""
    label = owl.locstr("has buffer size", "en")
    domain = [Device]
    range = [int]
    
  class Axis(Component):
    """An axis in the MTConnect ontology."""
    label = owl.locstr("Axis", "en")
    
  class Linear(Axis):
    """A linear axis in the MTConnect ontology."""
    label = owl.locstr("Linear Axis", "en")
    
  class Rotary(Axis):
    """A rotary axis in the MTConnect ontology."""
    label = owl.locstr("Rotary Axis", "en")
  
  class Controller(Component):
    """A controller in the MTConnect ontology."""
    label = owl.locstr("Controller", "en")
    
  class Path(Controller):
    """A path in the MTConnect ontology."""
    label = owl.locstr("Path", "en")
    
  # Systems
  class System(Component):
    """A system in the MTConnect ontology."""
    label = owl.locstr("System", "en")
    
  class Elecric(System):
    """An electric system in the MTConnect ontology."""
    label = owl.locstr("Electric System", "en")
    
  class Hydraulic(System):
    """A hydraulic system in the MTConnect ontology."""
    label = owl.locstr("Hydraulic System", "en")
    
  class Pneumatic(System):
    """A pneumatic system in the MTConnect ontology."""
    label = owl.locstr("Pneumatic System", "en")
    
  class Coolant(System):
    """A coolant system in the MTConnect ontology."""
    label = owl.locstr("Coolant System", "en")
    
  class Lubrication(System):
    """A lubrication system in the MTConnect ontology."""
    label = owl.locstr("Lubrication System", "en")
  
  # Auxiliaries
  class Auxiliary(Component):
    """An auxiliary in the MTConnect ontology."""
    label = owl.locstr("Auxiliary", "en")
    
  class Environmental(Auxiliary):
    """An environmental auxiliary in the MTConnect ontology."""
    label = owl.locstr("Environmental Auxiliary", "en")
    
  class Resource(Component):
    """A resource in the MTConnect ontology."""
    label = owl.locstr("Resource", "en")
    
  class Personnel(Resource):
    """A personnel resource in the MTConnect ontology."""
    label = owl.locstr("Personnel Resource", "en")
    
  class Materials(Resource):
    """A material resource in the MTConnect ontology."""
    label = owl.locstr("Material Resource", "en")
    
  class Stock(Materials):
    """A stock material resource in the MTConnect ontology."""
    label = owl.locstr("Stock Material Resource", "en")
  
  class Enclosure(Component):
    """An enclosure in the MTConnect ontology."""
    label = owl.locstr("Enclosure", "en")
    
  # Aggregators
  class Aggregator(Component):
    """An aggregator in the MTConnect ontology."""
    label = owl.locstr("Aggregator", "en")
  
  class Axes(Aggregator):
    """A collection of axes in the MTConnect ontology."""
    label = owl.locstr("Axes", "en")

  class Systems(Aggregator):
    """A collection of systems in the MTConnect ontology."""
    label = owl.locstr("Systems", "en")
    
  class Auxieliaries(Aggregator):
    """A collection of auxiliaries in the MTConnect ontology."""
    label = owl.locstr("Auxiliaries", "en")

  class Resources(Aggregator):
    """A collection of resources in the MTConnect ontology."""
    label = owl.locstr("Resources", "en")
    
  class Materials(Aggregator):
    """A collection of materials in the MTConnect ontology."""
    label = owl.locstr("Materials", "en")

MTConnect.save(file = "mtconnect.rdf", format = "rdfxml")