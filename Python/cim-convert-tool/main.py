import xml.etree.ElementTree as ET
import json
from xmlHelperCim17 import textImport, attributeImport, prefixListReplacer, prefixTagReplacer, refsXmlToJsonLdConverter, textsXmlToJsonLdConverter
from configEqCim17 import configEqCim17
from configSshCim17 import configSshCim17
from contextData import contextDataClass
from documentData import documentDataClass
import os

#--------Parameters---------#
cimFileType = "SSH"
cimFileLevel = "MV1"
#---------------------------#

# Do not Touch
docTitle = f"DIGIN10-30-{cimFileLevel}_{cimFileType}"
companyUuid = "bd53cf0a-2e2f-4230-a591-0233290b5f9b"
companyName = "Digin"
isVersionOfUrl = "https://digin.no/baseprofile/"

if cimFileType == "EQ":
    config = configEqCim17
elif cimFileType == "SSH":
    config = configSshCim17

dir_path = os.path.dirname(os.path.realpath(__file__))

inputFilePath = f"{dir_path}\Data\CIMXML\DIGIN10-30-{cimFileLevel}_{cimFileType}.xml" # Need to add relative path
outputFilePath = f"{dir_path}\Data\JSON-LD\DIGIN10-30-{cimFileLevel}_{cimFileType}.jsonld" # Need to add relative path

rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
cim = "http://iec.ch/TC57/CIM100#"
md = "http://iec.ch/TC57/61970-552/ModelDescription/1#"
eu = "http://iec.ch/TC57/CIM100-European#"

OutputJsonLD = {}

# Context
jsonldContext = contextDataClass(rdf, cim, md, eu) \
    .contextDataFunc()

OutputJsonLD["@context"] = jsonldContext
graphList = []

# FullModel
documentDataClass(
    inputFilePath,
    docTitle,
    companyUuid,
    companyName,
    isVersionOfUrl,
    cimFileType,
    OutputJsonLD
    ).documentDataFunc()

# xmlInput
tree = ET.parse(inputFilePath)
root = tree.getroot()

# SubClasses
for i in range(0, len(config)):

    importCimClasses = prefixListReplacer(list(config.keys()), cim, eu, rdf, md) # Adding full prefix for import
    importCimClass = importCimClasses[i]
    cim17ClassList = list(config.keys())[i] # --> ClassName

    for cimClass in root.findall(importCimClass):
        
        attributes = []
        texts = []
        textTypes = []
        refs = []

        cim17AttributeList = config[cim17ClassList]['attributes']
        cim17TagsList = []
        cim17RefsList = config[cim17ClassList]['refs']

        importAttributes = prefixListReplacer(config[cim17ClassList]['attributes'], cim, eu, rdf, md)

        importTags = []
        importTagsList = config[cim17ClassList]['tags']
        for i in range(0, len(importTagsList)):
            importTags.append(prefixTagReplacer(importTagsList[i][0], cim, eu, rdf, md))
            cim17TagsList.append(importTagsList[i][0])
            textTypes.append(importTagsList[i][1])

        importRefs = prefixListReplacer(config[cim17ClassList]['refs'], cim, eu, rdf, md)

        for i in range(0, len(importAttributes)):
            attributes.append(cimClass.get(importAttributes[i]))
        for i in range(0, len(importTags)):
            texts.append(textImport(cimClass, importTags[i]))
        for i in range(0, len(importRefs)):
            refs.append(attributeImport(cimClass, importRefs[i], '{' + rdf + '}' + 'resource'))

        jsonObject = {}

        for i in range(0, len(attributes)):
            jsonObject['@id'] = attributes[i].replace('_', 'urn:uuid:').replace('#', '')
            jsonObject['@type'] = cim17ClassList

        for i in range(0, len(texts)):
            textsXmlToJsonLdConverter(jsonObject, cim17TagsList[i], texts[i], textTypes[i])

        for i in range(0, len(refs)):
            refsXmlToJsonLdConverter(jsonObject, cim17RefsList[i], refs[i])
        
        graphList.append(jsonObject)

    OutputJsonLD["@graph"] = graphList

# Converting output to json
json_data = json.dumps(OutputJsonLD, indent=4, ensure_ascii=False)

# Printing result
# print(json_data)

# Writing to file
with open(outputFilePath, "w", encoding='utf8') as outfile:
    outfile.write(json_data)