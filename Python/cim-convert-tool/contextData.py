class contextDataClass:
    def __init__(self, isSkos):
        if isSkos == True:
            self.context = \
                {
                    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                    "cim": "http://ucaiug.org/ns/CIM#", # "http://iec.ch/TC57/CIM100#",
                    # "md": "http://iec.ch/TC57/61970-552/ModelDescription/1#",
                    "eu": "http://iec.ch/TC57/CIM100-European#",
                    "skos": "http://www.w3.org/2004/02/skos/core#",
                    "dcterms": "http://purl.org/dc/terms/",
                    "dcat": "http://www.w3.org/ns/dcat#",
                    "prov": "http://www.w3.org/ns/prov#",
                    "xsd": "http://www.w3.org/2001/XMLSchema#"
                }
        else:
            self.context = \
                {
                    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                    "cim": "http://ucaiug.org/ns/CIM#", # "http://iec.ch/TC57/CIM100#",
                    # "md": "http://iec.ch/TC57/61970-552/ModelDescription/1#",
                    "eu": "http://iec.ch/TC57/CIM100-European#",
                    "dcterms": "http://purl.org/dc/terms/",
                    "dcat": "http://www.w3.org/ns/dcat#",
                    "prov": "http://www.w3.org/ns/prov#",
                    "xsd": "http://www.w3.org/2001/XMLSchema#"
                }

    def contextDataFunc(self):
        return self.context