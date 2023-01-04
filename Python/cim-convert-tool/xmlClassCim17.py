import xml.etree.ElementTree as ET
from xmlHelperCim17 import textExport, attributeExport

class rdfClass:
    def __init__(self,
                 xmlns_rdf, xmlns_cim, xmlns_md, xmlns_eu):

        self.rdf = ET.Element('rdf:RDF')
        self.rdf.set('xmlns:rdf', xmlns_rdf)
        self.rdf.set('xmlns:cim', xmlns_cim)
        self.rdf.set('xmlns:md', xmlns_md)
        self.rdf.set('xmlns:eu', xmlns_eu)

    def rdfFunc(self):
        return self.rdf

class OutputCim17Class:
    def __init__(
        self,
        fatherTag,
        cimClass,
        cim17Attributes, cim17Attribute_values, cim17Tag, cim17_Texts, cim17Tag_Ref, cim17_Refs
        ):

        self.CIMClass = ET.SubElement(fatherTag, cimClass)
            
        for i in range(0, len(cim17Attributes)):
            self.CIMClass.set(cim17Attributes[i], cim17Attribute_values[i])

        for i in range(0, len(cim17Tag)):
            textExport(cim17_Texts[i], self.CIMClass, cim17Tag[i])

        for i in range(0, len(cim17Tag_Ref)):
            attributeExport(cim17_Refs[i], self.CIMClass, cim17Tag_Ref[i], 'rdf:resource')

    def OutputCim17Func(self):
        return self.CIMClass