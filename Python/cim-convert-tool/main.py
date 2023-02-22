import defusedxml.ElementTree as ET
import json
from functions import xmlPrefixListReplacer, valueDataTypeConverter
from configEqCim17 import configEqCim17
from configSshCim17 import configSshCim17
from configAsCim17 import configAsCim17
from configBaseVoltageCim17 import configBaseVoltageCim17
from configGeographicalRegionCim17 import configGeographicalRegionCim17
from configBmCim17 import configBmCim17
from configDlCim17 import configDlCim17
from configGlCim17 import configGlCim17
from configOpCim17 import configOpCim17
from configScCim17 import configScCim17
from configAcCim17 import configAcCim17
from configMeasurementValueSourceCim17 import configMeasurementValueSourceCim17
from configReadingQualityTypeCim17 import configReadingQualityTypeCim17
from configReadingTypeCim17 import configReadingTypeCim17
from configCuCim17 import configCuCim17
from configSvCim17 import configSvCim17
from configTpCim17 import configTpCim17
from configOrCim17 import configOrCim17
from contextData import contextDataClass
from documentData import documentDataClass
import os

#--------Parameters---------#
cimFileType = "EQ" # EQ, SSH, AS, RD, BM, DL, GL, OP, SC, AC, CU, SV, TP, OR
cimFileLevel = "LV1" #LV1, MV1, BaseVoltage, GeographicalRegion, HV1-MV1, MV1-LV1, M1, MeasurementValueSource, ReadingQualityType, ReadingType
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
elif cimFileType == "AS":
    config = configAsCim17
elif cimFileType == "RD" and cimFileLevel == "BaseVoltage":
    config = configBaseVoltageCim17
elif cimFileType == "RD" and cimFileLevel == "GeographicalRegion":
    config = configGeographicalRegionCim17
elif cimFileType == "BM":
    config = configBmCim17
elif cimFileType == "DL":
    config = configDlCim17
elif cimFileType == "GL":
    config = configGlCim17
elif cimFileType == "OP":
    config = configOpCim17
elif cimFileType == "SC":
    config = configScCim17
elif cimFileType == "AC":
    config = configAcCim17
elif cimFileType == "RD" and cimFileLevel == "MeasurementValueSource":
    config = configMeasurementValueSourceCim17
elif cimFileType == "RD" and cimFileLevel == "ReadingQualityType":
    config = configReadingQualityTypeCim17
elif cimFileType == "RD" and cimFileLevel == "ReadingType":
    config = configReadingTypeCim17
elif cimFileType == "CU":
    config = configCuCim17
elif cimFileType == "SV":
    config = configSvCim17
elif cimFileType == "TP":
    config = configTpCim17
elif cimFileType == "OR":
    config = configOrCim17

dir_path = os.path.dirname(os.path.realpath(__file__))

inputFilePath = f"{dir_path}\Data\CIMXML\DIGIN10-30-{cimFileLevel}_{cimFileType}.xml"
outputFilePath = f"{dir_path}\Data\JSON-LD\DIGIN10-30-{cimFileLevel}_{cimFileType}.jsonld"

rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
cim = "http://iec.ch/TC57/CIM100#"
md = "http://iec.ch/TC57/61970-552/ModelDescription/1#"
eu = "http://iec.ch/TC57/CIM100-European#"
skos = "http://www.w3.org/2004/02/skos/core#"
nc = "http://entsoe.eu/ns/nc#"

OutputJsonLD = {}

# Context

if cimFileType == "RD" and cimFileLevel == "ReadingQualityType":
    isSkos = True
elif cimFileType == "RD" and cimFileLevel == "ReadingType":
    isSkos = True
else:
    isSkos = False

if cimFileType == "OR":
    isNc = True
else:
    isNc = False

jsonldContext = contextDataClass(isSkos, isNc) \
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

xmlMainTagList = xmlPrefixListReplacer(list(config.keys()), cim, eu, rdf, md, skos, nc)
configMainTagList = list(config.keys())

for i in range(0, len(configMainTagList)):
    xmlMainTag = xmlMainTagList[i]
    configMainTag = configMainTagList[i]

    for mainTags in root.findall(xmlMainTag):
        xmlMainAttributeList = xmlPrefixListReplacer(list(config[configMainTag]['mainAttributes'].keys()), cim, eu, rdf, md, skos, nc)
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
        xmlTagList = xmlPrefixListReplacer(list(config[configMainTag]['tags'].keys()), cim, eu, rdf, md, skos, nc)
        configTagList = list(config[configMainTag]['tags'].keys())

        for i in range(0, len(xmlTagList)):
            xmlTag = xmlTagList[i]
            configTag = configTagList[i]

            textType = config[configMainTag]['tags'][configTag]['type']
            textList = config[configMainTag]['tags'][configTag]['list']

            if textList == True: # Checking if Tag can be list
                dictionaryClass[configTag] = []

            for tags in mainTags.findall(xmlTag):
                
                textValue = tags.text

                if configTag == 'cim:IdentifiedObject.mRID':
                    textValue = f'urn:uuid:{textValue}'
                elif configTag == 'nc:Name.mRID':
                    textValue = f'urn:uuid:{textValue}'
                elif configTag == 'nc:NameType.mRID':
                    textValue = f'urn:uuid:{textValue}'
                elif configTag == 'nc:NameTypeAuthority.mRID':
                    textValue = f'urn:uuid:{textValue}'

                if textList == True: # Checking if Tag can be list
                    if 'CIMDatatype' in config[configMainTag]['tags'][configTag].keys(): # Checking if Tag has CIMDatatype
                        dictionaryClass[configTag].append({config[configMainTag]['tags'][configTag]['CIMDatatype']: valueDataTypeConverter(textValue, textType)})
                    else:
                        dictionaryClass[configTag].append(valueDataTypeConverter(textValue, textType))
                else:
                    if 'CIMDatatype' in config[configMainTag]['tags'][configTag].keys(): # Checking if Tag has CIMDatatype
                        dictionaryClass[configTag] = {config[configMainTag]['tags'][configTag]['CIMDatatype']: valueDataTypeConverter(textValue, textType)}
                    else:
                        dictionaryClass[configTag] = valueDataTypeConverter(textValue, textType)
        
        # Attributes ##########################################
        xmlAttributeTagList = xmlPrefixListReplacer(list(config[configMainTag]['attributes'].keys()), cim, eu, rdf, md, skos, nc)
        configAttributeTagList = list(config[configMainTag]['attributes'].keys())

        for i in range(0, len(xmlAttributeTagList)):
            xmlAttributeTag = xmlAttributeTagList[i]
            configAttributeTag = configAttributeTagList[i]

            attributeList = config[configMainTag]['attributes'][configAttributeTag]['list']

            if attributeList == True:
                    dictionaryClass[configAttributeTag] = []

            for attributeTags in mainTags.findall(xmlAttributeTag):
                
                xmlAttributeSubTagList = xmlPrefixListReplacer(list(config[configMainTag]['attributes'][configAttributeTag].keys()), cim, eu, rdf, md, skos, nc)
                configAttributeSubTagList = list(config[configMainTag]['attributes'][configAttributeTag].keys())

                for i in range(0, len(xmlAttributeSubTagList)):
                    xmlAttributeSubTag = xmlAttributeSubTagList[i]
                    configAttributeSubTag = configAttributeSubTagList[i]
                    
                    if attributeTags.get(xmlAttributeSubTag) != None:
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