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
  'AVAILABILITY': MTConnect.Availability,
  'ASSET_ADDED': MTConnect.AssetAdded,
  'ASSET_CHANGED': MTConnect.AssetChanged,
  'ASSET_REMOVED': MTConnect.AssetRemoved,
  'TEMPERATURE': MTConnect.Temperature,
  'POSITION': MTConnect.Position,
  'POSITION:ACTUAL': MTConnect.PositionActual,
  'POSITION:COMMANDED': MTConnect.PositionCommanded,
  'LENGTH': MTConnect.Length,
  'ANGLE': MTConnect.Angle,
  'ANGLE:ACTUAL': MTConnect.AngleActual,
  'ANGLE:COMMANDED': MTConnect.AngleCommanded,
  'VELOCITY': MTConnect.Velocity,
  'VELOCITY_PROGRAMMED': MTConnect.VelocityProgrammed,
  'VELOCITY_RAPID': MTConnect.VelocityRapid,
  'ROTARY_VELOCITY': MTConnect.RotaryVelocity,
  'PATH_FEEDRATE': MTConnect.PathFeedrate,
  'PATH_FEEDRATE': MTConnect.PathFeedrateActual,
  'LINEAR_FORCE': MTConnect.Force,
  'PATH_POSITION': MTConnect.PathPosition,
  'PATH_POSITION': MTConnect.PathPositionActual,
  'PATH_POSITION': MTConnect.PathPositionCommanded,
  'CONTROLLER_MODE': MTConnect.ControllerMode,
  'EXECUTION': MTConnect.Execution,
  'CHUCK_STATE': MTConnect.ChuckState
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