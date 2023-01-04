import xml.etree.ElementTree as ET
import json
from xmlHelperCim17 import textImport, attributeImport, prefixListReplacer, prefixTagReplacer, refsXmlToJsonLdConverter, textsXmlToJsonLdConverter
from xmlConfigCim17 import xmlConfigCim17
from jsonldClassCim17 import contextClass
# import re

inputFilePath = "Python\cim-convert-tool\Data\CIMXML\DIGIN10-30-MV1_EQ.xml"
outputFilePath = "Python\cim-convert-tool\Data\JSON-LD\DIGIN10-30-MV1_EQ.jsonld"

rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
cim = "http://iec.ch/TC57/CIM100#"
md = "http://iec.ch/TC57/61970-552/ModelDescription/1#"
eu = "http://iec.ch/TC57/CIM100-European#"

OutputJsonLD = {}

#Context
jsonldContext = contextClass(rdf, cim, md, eu) \
    .contextFunc()

OutputJsonLD["@context"] = jsonldContext
graphList = []

#xmlInput
tree = ET.parse(inputFilePath)
root = tree.getroot()

# SubClasses
for i in range(0, len(xmlConfigCim17)):

    importCimClasses = prefixListReplacer(list(xmlConfigCim17.keys()), cim, eu, rdf, md) # Adding full prefix for import
    importCimClass = importCimClasses[i]
    cim17ClassList = list(xmlConfigCim17.keys())[i] # --> ClassName

    for cimClass in root.findall(importCimClass):
        
        attributes = []
        texts = []
        textTypes = []
        refs = []

        cim17AttributeList = xmlConfigCim17[cim17ClassList]['attributes']
        cim17TagsList = []
        cim17RefsList = xmlConfigCim17[cim17ClassList]['refs']

        importAttributes = prefixListReplacer(xmlConfigCim17[cim17ClassList]['attributes'], cim, eu, rdf, md)

        importTags = []
        importTagsList = xmlConfigCim17[cim17ClassList]['tags']
        for i in range(0, len(importTagsList)):
            importTags.append(prefixTagReplacer(importTagsList[i][0], cim, eu, rdf, md))
            cim17TagsList.append(importTagsList[i][0])
            textTypes.append(importTagsList[i][1])

        importRefs = prefixListReplacer(xmlConfigCim17[cim17ClassList]['refs'], cim, eu, rdf, md)

        for i in range(0, len(importAttributes)):
            attributes.append(cimClass.get(importAttributes[i]))
        for i in range(0, len(importTags)):
            texts.append(textImport(cimClass, importTags[i]))
        for i in range(0, len(importRefs)):
            refs.append(attributeImport(cimClass, importRefs[i], '{' + rdf + '}' + 'resource'))

        jsonObject = {}

        for i in range(0, len(attributes)):
            jsonObject['@id'] = attributes[i].replace('_', 'urn:uuid:')
            jsonObject['@type'] = cim17ClassList

        for i in range(0, len(texts)):
            textsXmlToJsonLdConverter(jsonObject, cim17TagsList[i], texts[i], textTypes[i])

        for i in range(0, len(refs)):
            refsXmlToJsonLdConverter(jsonObject, cim17RefsList[i], refs[i])
        
        graphList.append(jsonObject)

    OutputJsonLD["@graph"] = graphList

# Converting output to json
json_data = json.dumps(OutputJsonLD)

# Loading outup json
json_object = json.loads(json_data)

# Formatting json
json_dumps = json.dumps(json_object, indent=4)

# Printing result
# print(json_dumps)

# Writing to file
with open(outputFilePath, "w") as outfile:
    outfile.write(json_dumps)