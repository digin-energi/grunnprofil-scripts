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