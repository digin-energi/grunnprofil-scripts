class contextDataClass:
    def __init__(self, rdfVar, cimVar, mdVar, euVar):
        self.context = \
            {
                "rdf": rdfVar,
                "cim": cimVar,
                "md": mdVar,
                "eu": euVar,
                "dcterms": "http://purl.org/dc/terms/",
                "dcat": "http://www.w3.org/ns/dcat#",
                "prov": "http://www.w3.org/ns/prov#",
                "xsd": "http://www.w3.org/2001/XMLSchema#"
            }

    def contextDataFunc(self):
        return self.context