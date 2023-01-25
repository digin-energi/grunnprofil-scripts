configSshCim17 = \
    {
        'cim:ACLineSegment': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:Breaker': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False},
                'cim:Switch.locked': {'type': 'bool', 'list': False},
                'cim:Switch.open': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:BusbarSection': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:ConformLoad': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False},
                'cim:EnergyConsumer.p': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:EnergyConsumer.q': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'}
            },
            'attributes': {

            }
        },
        'cim:ControlArea': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:ControlArea.netInterchange': {'type': 'float', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:CurrentLimit': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:CurrentLimit.value': {'type': 'float', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:Disconnector': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False},
                'cim:Switch.locked': {'type': 'bool', 'list': False},
                'cim:Switch.open': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:EquivalentInjection': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False},
                'cim:EquivalentInjection.p': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:EquivalentInjection.q': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'}
            },
            'attributes': {

            }
        },
        'cim:Fuse': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False},
                'cim:Switch.locked': {'type': 'bool', 'list': False},
                'cim:Switch.open': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:GeneratingUnit': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:LinearShuntCompensator': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:LoadBreakSwitch': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False},
                'cim:Switch.locked': {'type': 'bool', 'list': False},
                'cim:Switch.open': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:PetersenCoil': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:PowerTransformer': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:SynchronousMachine': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:Equipment.inService': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:Terminal': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:ACDCTerminal.connected': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        }
    }