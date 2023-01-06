cim_IdentifiedObject = \
    [
        ['cim:IdentifiedObject.mRID', 'string'],
        ['cim:IdentifiedObject.description', 'string'],
        ['cim:IdentifiedObject.name', 'string']
    ]
cim_Equipment = \
    [
        ['cim:Equipment.aggregate', 'bool'],
        #['cim:Equipment.networkAnalysisEnabled', 'bool'],
        ['cim:Equipment.normallyInService', 'bool']
    ]
cim_Switch = \
    [
        ['cim:Switch.locked', 'bool'],
        ['cim:Switch.normalOpen', 'bool'],
        ['cim:Switch.ratedCurrent', 'float'],
        ['cim:Switch.retained', 'bool']
    ]

configEqCim17 = \
    {
        'cim:ACLineSegment': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
            [
                ['cim:Conductor.length', 'float'],
                ['cim:ACLineSegment.bch', 'float'],
                ['cim:ACLineSegment.gch', 'float'],
                #['cim:ACLineSegment.r0', 'float'],
                ['cim:ACLineSegment.r', 'float'],
                ['cim:ACLineSegment.x', 'float']
            ],
            'refs': [
                'cim:Equipment.EquipmentContainer',
                'cim:ConductingEquipment.BaseVoltage'
            ]
        },
        'cim:Bay': {
            'attributes': [
                'rdf:ID'
            ],
            'tags': cim_IdentifiedObject,
            'refs': [
                'cim:Bay.VoltageLevel'
            ]
        },
        'cim:Breaker': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
                cim_Switch,
            'refs': [
                'cim:Equipment.EquipmentContainer',
                'cim:ConductingEquipment.BaseVoltage'
            ]
        },
        'cim:BusbarSection': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment,
            'refs': [
                'cim:Equipment.EquipmentContainer',
                'cim:ConductingEquipment.BaseVoltage'
            ]
        },
        'cim:ConformLoad': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
            [
                ['cim:EnergyConsumer.pfixed', 'float'],
                ['cim:EnergyConsumer.pfixedPct', 'float'],
                ['cim:EnergyConsumer.qfixed', 'float'],
                ['cim:EnergyConsumer.qfixedPct', 'float']
            ],
            'refs': [
                'cim:Equipment.EquipmentContainer',
                'cim:ConductingEquipment.BaseVoltage',
                'cim:ConformLoad.LoadGroup'
            ]
        },
        'cim:ConformLoadGroup': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                'cim:LoadGroup.SubLoadArea'
            ]
        },
        'cim:ConnectivityNode': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                'cim:ConnectivityNode.ConnectivityNodeContainer'
            ]
        },
        'cim:ControlArea': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                'cim:ControlArea.EnergyArea',
                'cim:ControlArea.type'
            ]
        },
        'cim:CurrentLimit': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                [
                    ['cim:CurrentLimit.normalValue', 'float']
                ],
            'refs': [
                'cim:OperationalLimit.OperationalLimitSet',
                'cim:OperationalLimit.OperationalLimitType'
            ]
        },
        'cim:Disconnector': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
                cim_Switch,
            'refs': [
                'cim:Equipment.EquipmentContainer',
                'cim:ConductingEquipment.BaseVoltage'
            ]
        },
        'cim:EquivalentInjection': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
                [
                    ['cim:EquivalentInjection.maxP', 'float'],
                    ['cim:EquivalentInjection.maxQ', 'float'],
                    ['cim:EquivalentInjection.minP', 'float'],
                    ['cim:EquivalentInjection.minQ', 'float'],
                    ['cim:EquivalentInjection.regulationCapability', 'bool']
                ],
            'refs': [
                'cim:ConductingEquipment.BaseVoltage'
            ]
        },
        'cim:Fuse': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
                cim_Switch,
            'refs': [
                'cim:Equipment.EquipmentContainer',
                'cim:ConductingEquipment.BaseVoltage'
            ]
        },
        'cim:GeneratingUnit': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
                [
                    ['cim:GeneratingUnit.highControlLimit', 'float'],
                    ['cim:GeneratingUnit.initialP', 'float'],
                    ['cim:GeneratingUnit.lowControlLimit', 'float'],
                    ['cim:GeneratingUnit.maxEconomicP', 'float'],
                    ['cim:GeneratingUnit.maxOperatingP', 'float'],
                    ['cim:GeneratingUnit.minEconomicP', 'float'],
                    ['cim:GeneratingUnit.minOperatingP', 'float'],
                    ['cim:GeneratingUnit.nominalP', 'float'],
                    ['cim:GeneratingUnit.ratedGrossMaxP', 'float'],
                    ['cim:GeneratingUnit.ratedNetMaxP', 'float']
                ],
            'refs': [
                'cim:Equipment.EquipmentContainer'
            ]
        },
        'cim:Line': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                
            ]
        },
        'cim:LinearShuntCompensator': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
                [
                    ['cim:ShuntCompensator.aVRDelay', 'float'],
                    ['cim:ShuntCompensator.maximumSections', 'int'],
                    ['cim:ShuntCompensator.nomU', 'float'],
                    ['cim:ShuntCompensator.normalSections', 'int'],
                    ['cim:LinearShuntCompensator.bPerSection', 'float'],
                    ['cim:LinearShuntCompensator.gPerSection', 'float']
                ],
            'refs': [
                'cim:Equipment.EquipmentContainer',
                'cim:RegulatingCondEq.RegulatingControl'
            ]
        },
        'cim:LoadArea': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                
            ]
        },
        'cim:LoadBreakSwitch': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
                cim_Switch,
            'refs': [
                'cim:Equipment.EquipmentContainer',
                'cim:ConductingEquipment.BaseVoltage'
            ]
        },
        'cim:LoadResponseCharacteristic': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                [
                    ['cim:LoadResponseCharacteristic.pConstantPower', 'float'],
                    ['cim:LoadResponseCharacteristic.pConstantCurrent', 'float'],
                    ['cim:LoadResponseCharacteristic.pConstantImpedance', 'float'],
                    ['cim:LoadResponseCharacteristic.qConstantPower', 'float'],
                    ['cim:LoadResponseCharacteristic.qConstantCurrent', 'float'],
                    ['cim:LoadResponseCharacteristic.qConstantImpedance', 'float'],
                    ['cim:LoadResponseCharacteristic.exponentModel', 'bool']
                ],
            'refs': [
                
            ]
        },
        'cim:OperationalLimitSet': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                'cim:OperationalLimitSet.Terminal'
            ]
        },
        'cim:OperationalLimitType': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                [
                    ['cim:OperationalLimitType.acceptableDuration', 'float'],
                    ['cim:OperationalLimitType.isInfiniteDuration',  'bool']
                ],
            'refs': [
                'cim:OperationalLimitType.direction',
                'eu:OperationalLimitType.kind'
            ]
        },
        'cim:PetersenCoil': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment,
            'refs': [
                'cim:Equipment.EquipmentContainer'
            ]
        },
        'cim:PowerTransformer': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
                [
                    ['cim:PowerTransformer.isPartOfGeneratorUnit',  'bool']
                ],
            'refs': [
                'cim:Equipment.EquipmentContainer'
            ]
        },
        'cim:PowerTransformerEnd': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                [
                    ['cim:TransformerEnd.endNumber',  'int'],
                    ['cim:TransformerEnd.grounded',  'bool'],
                    ['cim:PowerTransformerEnd.b',  'float'],
                    ['cim:PowerTransformerEnd.r',  'float'],
                    ['cim:PowerTransformerEnd.ratedS',  'float'],
                    ['cim:PowerTransformerEnd.ratedU',  'float'],
                    ['cim:PowerTransformerEnd.x',  'float']
                ],
            'refs': [
                'cim:TransformerEnd.BaseVoltage',
                'cim:TransformerEnd.Terminal',
                'cim:PowerTransformerEnd.connectionKind',
                'cim:PowerTransformerEnd.PowerTransformer'
            ]
        },
        'cim:RatioTapChanger': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                [
                    ['cim:TapChanger.highStep',  'int'],
                    ['cim:TapChanger.lowStep',  'int'],
                    ['cim:TapChanger.ltcFlag',  'bool'],
                    ['cim:TapChanger.neutralStep',  'int'],
                    ['cim:TapChanger.neutralU',  'float'],
                    ['cim:TapChanger.normalStep',  'int'],
                    ['cim:RatioTapChanger.stepVoltageIncrement',  'float']
                ],
            'refs': [
                'cim:TapChanger.TapChangerControl',
                'cim:RatioTapChanger.tculControlMode',
                'cim:RatioTapChanger.TransformerEnd'
            ]
        },
        'cim:RegulatingControl': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                'cim:RegulatingControl.mode',
                'cim:RegulatingControl.Terminal'
            ]
        },
        'cim:SubGeographicalRegion': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                'cim:SubGeographicalRegion.Region'
            ]
        },
        'cim:SubLoadArea': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                'cim:SubLoadArea.LoadArea'
            ]
        },
        'cim:Substation': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                'cim:Substation.Region'
            ]
        },
        'cim:SynchronousMachine': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                cim_Equipment +
                [
                    ['cim:SynchronousMachine.maxQ',  'float'],
                    ['cim:SynchronousMachine.maxU',  'float'],
                    ['cim:SynchronousMachine.minQ',  'float'],
                    ['cim:SynchronousMachine.minU',  'float'],
                    ['cim:SynchronousMachine.qPercent',  'float'],
                    ['cim:SynchronousMachine.r',  'float'],
                    ['cim:SynchronousMachine.referencePriority',  'int'],
                    ['cim:RotatingMachine.ratedS',  'float']
                ],
            'refs': [
                'cim:SynchronousMachine.type',
                'cim:Equipment.EquipmentContainer',
                'cim:RegulatingCondEq.RegulatingControl',
                'cim:RotatingMachine.GeneratingUnit'
            ]
        },
        'cim:TapChangerControl': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                'cim:RegulatingControl.mode',
                'cim:RegulatingControl.Terminal'
            ]
        },
        'cim:Terminal': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject +
                [
                    ['cim:ACDCTerminal.sequenceNumber',  'int']
                ],
            'refs': [
                'cim:Terminal.phases',
                'cim:Terminal.ConductingEquipment',
                'cim:Terminal.ConnectivityNode'
            ]
        },
        'cim:VoltageLevel': {
            'attributes': [
                'rdf:ID'
            ],
            'tags':
                cim_IdentifiedObject,
            'refs': [
                'cim:VoltageLevel.BaseVoltage',
                'cim:VoltageLevel.Substation'
            ]
        }
    }
