from ontologies import *

'''
Units = {
  'NEWTON': QUDT.N,
  'NEWTON_METER': QUDT.N_M,
  'MILLIMETER': QUDT.MilliM,
  'DEGREE': QUDT.DEG,
  'MILLIMETER/SECOND': QUDT.MilliM_PER_SEC,
  'REVOLUTION/MINUTE': QUDT.RPM,
  'CELSIUS': QUDT.DEG_C
}
'''

Components = {
  'Linear': MTConnect.Linear,
  'Rotary': MTConnect.Rotary,
  'Device': MTConnect.Device,
  'Controller': MTConnect.Controller,
  'Path': MTConnect.Path,
  #'Composition': BFO.object,
  #'MOTOR': MTConnect.Motor,
  #'BALLSCREW': MTConnect.Ballscrew,
  'Electric': MTConnect.Electric,
  'Hydraulic': MTConnect.Hydraulic,
  'Pneumatic': MTConnect.Pneumatic,
  'Lubrication': MTConnect.Lubrication,
  'Stock': MTConnect.Stock,
  'Personnel': MTConnect.Personnel,
  #'PartOccurrence': MTConnect.ProductPart,
  #'Link': MTConnect.Structure,
  #'Enclosure': MTConnect.Structure,
  'Environmental': MTConnect.Room,
  'Door': MTConnect.Door,
  'Coolant': MTConnect.Coolant,
  #'Chuck': MTConnect.Chuck,

  'Axes': MTConnect.Axes,
  'Systems': MTConnect.Systems,
  #'Parts': MTConnect.Parts,
  'Auxiliaries': MTConnect.Auxiliaries,
  'Resources': MTConnect.Resources,
  #'Structures': False,
  'Materials': MTConnect.Materials
}

'''
Functions = {
  'Device': Example.MillingCapability,
  'PRISMATIC': Example.PrismaticMotionCapability,
  'REVOLUTE': Example.IndexedRevoluteCapability,
  'CONTINUOUS': Example.ContinuousRevoluteCapability
}

Capabilities = {
  'Device': Example.TurningCapability
}
'''

DataItems = {
  'AVAILABILITY': MTConnect.AvailabilityDataItem,
  'ASSET_ADDED': MTConnect.AssetAddedDataItem,
  'ASSET_CHANGED': MTConnect.AssetChangedDataItem,
  'ASSET_REMOVED': MTConnect.AssetRemovedDataItem,
  'TEMPERATURE': MTConnect.TemperatureDataItem,
  'POSITION': MTConnect.PositionDataItem,
  'POSITION:ACTUAL': MTConnect.PositionActualDataItem,
  'POSITION:COMMANDED': MTConnect.PositionCommandedDataItem,
  'LENGTH': MTConnect.LengthDataItem,
  'ANGLE': MTConnect.AngleDataItem,
  'ANGLE:ACTUAL': MTConnect.AngleActualDataItem,
  'ANGLE:COMMANDED': MTConnect.AngleCommandedDataItem,
  'VELOCITY': MTConnect.VelocityDataItem,
  'VELOCITY_PROGRAMMED': MTConnect.VelocityProgrammedDataItem,
  'VELOCITY_RAPID': MTConnect.VelocityRapidDataItem,
  'ROTARY_VELOCITY': MTConnect.RotaryVelocityDataItem,
  'PATH_FEEDRATE': MTConnect.PathFeedrateDataItem,
  'PATH_FEEDRATE': MTConnect.PathFeedrateActualDataItem,
  'LINEAR_FORCE': MTConnect.ForceDataItem,
  'PATH_POSITION': MTConnect.PathPositionDataItem,
  'PATH_POSITION:ACTUAL': MTConnect.PathPositionActualDataItem,
  'PATH_POSITION:COMMANDED': MTConnect.PathPositionCommandedDataItem,
  'PATH_FEEDRATE:ACTUAL': MTConnect.PathFeedrateActualDataItem,
  'PATH_FEEDRATE:COMMANDED': MTConnect.PathFeedrateCommandedDataItem,
  'PATH_FEEDRATE_OVERRIDE': MTConnect.PathFeedrateOverrideDataItem,
  'PATH_FEEDRATE_OVERRIDE:RAPID': MTConnect.PathFeedrateOverrideRapidDataItem,
  'PATH_FEEDRATE_OVERRIDE:PROGRAMMED': MTConnect.PathFeedrateOverrideProgrammedDataItem,
  'CONTROLLER_MODE': MTConnect.ControllerModeDataItem,
  'EXECUTION': MTConnect.ExecutionDataItem,
  'CHUCK_STATE': MTConnect.ChuckStateDataItem,
  'MATERIAL': MTConnect.MaterialDataItem,
  'SYSTEM_CONDITION': MTConnect.SystemConditionDataItem,
  'POSITION_CONDITION': MTConnect.PositionConditionDataItem,
  'TEMPERATURE_CONDITION': MTConnect.TemperatureConditionDataItem,
  'USER': MTConnect.UserDataItem
}

'''
Roles = {
  'Device': [Core.EquipmentRole, Example.EngineeredSystemRole],
  'Linear': [Example.EngineeredSystemRole],
  'Rotary': [Example.EngineeredSystemRole],
  'Controller': [Example.EngineeredSystemRole],
  'Path': [Example.EngineeredSystemRole],
  'Composition': [Example.MaterialArtifactRole],
  'MOTOR': [Example.MaterialArtifactRole],
  'BALLSCREW': [Example.MaterialArtifactRole],
  'Electric': [Example.EngineeredSystemRole],
  'Hydraulic': [Example.EngineeredSystemRole],
  'Pneumatic': [Example.EngineeredSystemRole],
  'Lubrication': [Example.EngineeredSystemRole],
  'Stock': [Example.MaterialArtifactRole],
  'PartOccurrence': [Example.MaterialArtifactRole],
  'Link': [Example.MaterialArtifactRole],
  'Enclosure': [Example.MaterialArtifactRole],
  'Door': [Example.MaterialArtifactRole],
  'Coolant': [Example.EngineeredSystemRole]
}

Separate = {
  Example.Room
}
'''

'''
Namespaces = {
    "http://purl.obolibrary.org/obo/": "bfo",
    "https://spec.industrialontologies.org/ontology/core/Core/": "core",
    "https://spec.industrialontologies.org/ontology/core/meta/AnnotationVocabulary/": "av",
    "https://www.omg.org/spec/Commons/Designators/": "des",
    "https://spec.industrialontologies.org/ontology/qualities/Qualities/": "qual",
    "https://spec.industrialontologies.org/ontology/qualities/Qualities-Physical/": "qp",
    "http://example.org/ontology/": "ex",
    "http://example.org/data/": "data",
    "http://qudt.org/vocab/unit/": "unit"
}
'''