import xml.etree.ElementTree as ET
import json
from functions import xmlPrefixListReplacer, valueDataTypeConverter
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
companyName = "DIGIN"
isVersionOfUrl = "https://digin.no/baseprofile/"

if cimFileType == "EQ":
    config = configEqCim17
elif cimFileType == "SSH":
    config = configSshCim17

dir_path = os.path.dirname(os.path.realpath(__file__))

inputFilePath = f"{dir_path}\Data\CIMXML\DIGIN10-30-{cimFileLevel}_{cimFileType}.xml"
outputFilePath = f"{dir_path}\Data\JSON-LD\DIGIN10-30-{cimFileLevel}_{cimFileType}.jsonld"

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

xmlMainTagList = xmlPrefixListReplacer(list(config.keys()), cim, eu, rdf, md)
configMainTagList = list(config.keys())

for i in range(0, len(configMainTagList)):
    xmlMainTag = xmlMainTagList[i]
    configMainTag = configMainTagList[i]

    for mainTags in root.findall(xmlMainTag):
        xmlMainAttributeList = xmlPrefixListReplacer(list(config[configMainTag]['mainAttributes'].keys()), cim, eu, rdf, md)
        configMainAttributeList = list(config[configMainTag]['mainAttributes'].keys())

        # MainAttributes ######################################
        dictionaryClass = {}

        for i in range(0, len(xmlMainAttributeList)):
            xmlMainAttribute = xmlMainAttributeList[i]
            configMainAttribute = configMainAttributeList[i]

            mainAttributeValue = f'urn:uuid:{mainTags.get(xmlMainAttribute)[1:]}'
            mainAttributeType = config[configMainTag]['mainAttributes'][configMainAttribute]['type']

            dictionaryClass["@id"] = valueDataTypeConverter(mainAttributeValue, mainAttributeType)
            dictionaryClass["@type"] = configMainTag

        # Tags ################################################
        xmlTagList = xmlPrefixListReplacer(list(config[configMainTag]['tags'].keys()), cim, eu, rdf, md)
        configTagList = list(config[configMainTag]['tags'].keys())

        for i in range(0, len(xmlTagList)):
            xmlTag = xmlTagList[i]
            configTag = configTagList[i]

            textType = config[configMainTag]['tags'][configTag]['type']
            textList = config[configMainTag]['tags'][configTag]['list']

            if textList == True:
                dictionaryClass[configTag] = []

            for tags in mainTags.findall(xmlTag):
                
                textValue = tags.text
    
                if textList == True:
                    dictionaryClass[configTag].append(valueDataTypeConverter(textValue, textType))
                else:
                    dictionaryClass[configTag] = valueDataTypeConverter(textValue, textType)
        
        # Attributes ##########################################
        xmlAttributeTagList = xmlPrefixListReplacer(list(config[configMainTag]['attributes'].keys()), cim, eu, rdf, md)
        configAttributeTagList = list(config[configMainTag]['attributes'].keys())

        for i in range(0, len(xmlAttributeTagList)):
            xmlAttributeTag = xmlAttributeTagList[i]
            configAttributeTag = configAttributeTagList[i]

            attributeList = config[configMainTag]['attributes'][configAttributeTag]['list']

            if attributeList == True:
                    dictionaryClass[configAttributeTag] = []

            for attributeTags in mainTags.findall(xmlAttributeTag):
                
                xmlAttributeSubTagList = xmlPrefixListReplacer(list(config[configMainTag]['attributes'][configAttributeTag].keys()), cim, eu, rdf, md)
                configAttributeSubTagList = list(config[configMainTag]['attributes'][configAttributeTag].keys())

                for i in range(0, len(xmlAttributeSubTagList)):
                    xmlAttributeSubTag = xmlAttributeSubTagList[i]
                    configAttributeSubTag = configAttributeSubTagList[i]

                    if attributeTags.get(xmlAttributeSubTag)[:2] == '#_':
                        attributeValue = f'urn:uuid:{attributeTags.get(xmlAttributeSubTag)[2:]}'
                    else:
                        attributeValue = attributeTags.get(xmlAttributeSubTag)
                        
                    attributeType = config[configMainTag]['attributes'][configAttributeTag][configAttributeSubTag]['type']

                    subDictionaryClass = {}
                    subDictionaryClass['@id'] = valueDataTypeConverter(attributeValue, attributeType)

                    if attributeList == True:
                        dictionaryClass[configAttributeTag].append(subDictionaryClass)
                    else:
                        dictionaryClass[configAttributeTag] = subDictionaryClass

        graphList.append(dictionaryClass)

OutputJsonLD["@graph"] = graphList

# Output

# Converting output to json
json_data = json.dumps(OutputJsonLD, indent=4, ensure_ascii=False)

# Printing result
# print(json_data)

# Writing to file
with open(outputFilePath, "w", encoding='utf8') as outfile:
    outfile.write(json_data)