cim_Equipment = \
    [
        ['cim:Equipment.inService', 'bool']
    ]
cim_Switch = \
    [
        ['cim:Switch.locked', 'bool'],
        ['cim:Switch.open', 'bool']
    ]

configSshCim17 = \
    {
        'cim:ACLineSegment': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment,
            'refs': [

            ]
        },
        'cim:Breaker': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment +
                cim_Switch,
            'refs': [

            ]
        },
        'cim:BusbarSection': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment,
            'refs': [

            ]
        },
        'cim:ConformLoad': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment +
                [
                    ['cim:EnergyConsumer.p', 'float'],
                    ['cim:EnergyConsumer.q', 'float']
                ],
            'refs': [

            ]
        },
        'cim:ControlArea': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                [
                    ['cim:ControlArea.netInterchange', 'float']
                ],
            'refs': [

            ]
        },
        'cim:CurrentLimit': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                [
                    ['cim:CurrentLimit.value', 'float']
                ],
            'refs': [

            ]
        },
        'cim:Disconnector': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment +
                cim_Switch,
            'refs': [

            ]
        },
        'cim:EquivalentInjection': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment +
                [
                    ['cim:EquivalentInjection.p', 'float'],
                    ['cim:EquivalentInjection.q', 'float']
                ],
            'refs': [

            ]
        },
        'cim:Fuse': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment +
                cim_Switch,
            'refs': [

            ]
        },
        'cim:GeneratingUnit': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment,
            'refs': [

            ]
        },
        'cim:LinearShuntCompensator': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment,
            'refs': [

            ]
        },
        'cim:LoadBreakSwitch': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment +
                cim_Switch,
            'refs': [

            ]
        },
        'cim:PetersenCoil': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment,
            'refs': [

            ]
        },
        'cim:PowerTransformer': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment,
            'refs': [

            ]
        },
        'cim:SynchronousMachine': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                cim_Equipment,
            'refs': [

            ]
        },
        'cim:Terminal': {
            'attributes': [
                'rdf:about'
            ],
            'tags':
                [
                    ['cim:ACDCTerminal.connected',  'bool']
                ],
            'refs': [

            ]
        }
    }
