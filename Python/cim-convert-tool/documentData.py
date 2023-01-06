import xml.etree.ElementTree as ET
from datetime import datetime

def modellInfoFunc(
    fullModelRdfAbout,
    fullModelModelCreated,
    docTitle,
    fullModelModelDescription,
    fullModelModelVersion,
    companyUuid,
    companyName,
    isVersionOfUrl,
    cimFileType,
    fullModelModelingAuthoritySet,
    fullModelProfileList,
    fullModelDependentOn,
    dictionary
    ):
    dateTimeNow = datetime.now().strftime("%Y-%m-%dT%H%M%SZ")
    yearNow = datetime.now().strftime("%Y")

    dictionary["@id"] = fullModelRdfAbout
    dictionary["prov:generatedAt"] = [
        {
            "@value": dateTimeNow,
            "@type": "http://www.w3.org/2001/XMLSchema#date"
        }
    ]
    dictionary["dcterm:created"] = [
        {
            "@value": fullModelModelCreated,
            "@type": "http://www.w3.org/2001/XMLSchema#date"
        }
    ]
    dictionary["dcterms:title"] = docTitle #DIGIN10-30-MV1_EQ
    dictionary["dcterms:description"] = [
        {
            "@value": fullModelModelDescription,
            "@language": "en"
        }
    ]
    dictionary["dcat:version"] = fullModelModelVersion
    dictionary["dcterms:publisher"] = [
        {
            "@id": f"urn:uuid:{companyUuid}", #Digin uuid
            "dcterms:title": companyName #Digin
        }
    ]
    dictionary["dcterms:rights"] = f"© {yearNow} Copyright"
    dictionary["dcterms:rightHolder"] = companyName
    dictionary["dcterms:license"] = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
    dictionary["dcterms:accessRights"] = "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
    dictionary["dcat:isVersionOf"] = f"{isVersionOfUrl}{docTitle}" #https://digin.no/baseprofile/DIGIN10-30-MV1_EQ
    dictionary["dcat:keyword"] = cimFileType #EQ
    dictionary["dcterms:LocationPeriodOrJurisdiction"] = fullModelModelingAuthoritySet
    dictionary["dcterms:conformsTo"] = fullModelProfileList
    dictionary["dcterms:references"] = [
        {
            "@id": fullModelDependentOn,
            "dcterms:title": docTitle #DIGIN10-30-MV1_EQ
        }
    ]
    return dictionary

class documentDataClass:
    def __init__(self,
                 inputFilePath, docTitle, companyUuid, companyName, isVersionOfUrl, cimFileType, dictionary):

        fullModelRdfAbout = ""
        fullModelModelCreated = ""
        fullModelModelDescription = ""
        fullModelModelVersion = ""
        fullModelModelingAuthoritySet = ""
        fullModelProfileList = []
        fullModelDependentOn = ""

        tree = ET.parse(inputFilePath)
        root = tree.getroot()

        childList = []
        for childs in root:
                childList.append(childs.tag)
                if childs.tag == '{http://iec.ch/TC57/61970-552/ModelDescription/1#}FullModel': break
        fullModelIndex = childList.index('{http://iec.ch/TC57/61970-552/ModelDescription/1#}FullModel')

        fullModelRdfAbout = root[0].get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about')
        for i in range(0, len(root[fullModelIndex])):
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.created": fullModelModelCreated = root[fullModelIndex][i].text
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.description": fullModelModelDescription = root[fullModelIndex][i].text
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.version": fullModelModelVersion = root[fullModelIndex][i].text
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.modelingAuthoritySet": fullModelModelingAuthoritySet = root[fullModelIndex][i].text
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.profile": fullModelProfileList.append(root[fullModelIndex][i].text)
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.DependentOn": fullModelDependentOn = root[fullModelIndex][i].get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource')

        self.fullModelJsonLd = modellInfoFunc(
                fullModelRdfAbout,
                fullModelModelCreated,
                docTitle,
                fullModelModelDescription,
                fullModelModelVersion,
                companyUuid,
                companyName,
                isVersionOfUrl,
                cimFileType,
                fullModelModelingAuthoritySet,
                fullModelProfileList,
                fullModelDependentOn,
                dictionary
                )

    def documentDataFunc(self):
        return self.fullModelJsonLd