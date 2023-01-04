from pickle import NONE

class contextClass:
    def __init__(self, rdfVar, cimVar, mdVar, euVar):
        self.context = \
            {
                "rdf": rdfVar,
                "cim": cimVar,
                "md": mdVar,
                "eu": euVar
            }

    def contextFunc(self):
        return self.context

class EQJsonLDClass:
    def __init__(self, contextJson,
                #  ACLineSegments, Bays, Breakers, BusbarSections, ConformLoads,
                #  ConformLoadGroups, ConnectivityNodes, CurrentLimits, EquivalentInjections, LoadAreas, Names, NameTypes,
                #  NameTypeAuthoritys, OperationalLimitSets, OperationalLimitTypes, SubGeographicalRegions, SubLoadAreas,
                #  Substations, Terminals, VoltageLevels
                 ):
        self.EQJsonLD = \
            {
                "@context": contextJson
                # "cim:ACLineSegment": ACLineSegments,
                # "cim:Bay": Bays,
                # "cim:Breaker": Breakers,
                # "cim:BusbarSection": BusbarSections,
                # "cim:ConfomLoad": ConformLoads,
                # "cim:ConformLoadGroup": ConformLoadGroups,
                # "cim:ConnectivityNode": ConnectivityNodes,
                # "cim:CurrentLimit": CurrentLimits,
                # "cim:EquivalentInjection": EquivalentInjections,
                # "cim:LoadArea": LoadAreas,
                # "cim:Name": Names,
                # "cim:NameType": NameTypes,
                # "cim:NameTypeAuthority": NameTypeAuthoritys,
                # "cim:OperationalLimitSet": OperationalLimitSets,
                # "cim:OperationalLimitType": OperationalLimitTypes,
                # "cim:SubGeographicalRegion": SubGeographicalRegions,
                # "cim:SubLoadArea": SubLoadAreas,
                # "cim:Substation": Substations,
                # "cim:Terminal": Terminals,
                # "cim:VoltageLevel": VoltageLevels
            }

    def EQJsonLDFunc(self):
        return self.EQJsonLD

class ACLineSegmentClass:
    def __init__(self, ID, description, name, aggregate, networkAnalysisEnabled, normallyInService, length, b0ch, bch,
                 g0ch, gch, r0, r, shortCircuitEndTemperature, x0, x, BaseVoltage):
        self.ACLineSegment = \
            {
                "@id": ID,
                "@type": "ACLineSegment",
                "cim:IdentifiedObject.mRID": ID.lstrip('_'),
                "cim:IdentifiedObject.description": description,
                "cim:IdentifiedObject.name": name,
                "cim:Equipment.aggregate": aggregate == "true",
                "cim:Equipment.networkAnalysisEnabled": networkAnalysisEnabled == "true",
                "cim:Equipment.normallyInService": normallyInService == "true",
                "cim:Conductor.length": float(length) if length != None else None,
                "cim:ACLineSegment.b0ch": float(b0ch) if b0ch != None else None,
                "cim:ACLineSegment.bch": float(bch) if bch != None else None,
                "cim:ACLineSegment.g0ch": float(g0ch) if g0ch != None else None,
                "cim:ACLineSegment.gch": float(gch) if gch != None else None,
                "cim:ACLineSegment.r0": float(r0) if r0 != None else None,
                "cim:ACLineSegment.r": float(r) if r != None else None,
                "cim:ACLineSegment.shortCircuitEndTemperature": float(shortCircuitEndTemperature),
                "cim:ACLineSegment.x0": float(x0) if x0 != None else None,
                "cim:ACLineSegment.x": float(x) if x != None else None,
                "cim:ConductingEquipment.BaseVoltage": {
                    "@id": BaseVoltage
                }
            }

    def ACLineSegmentFunc(self):
        return self.ACLineSegment