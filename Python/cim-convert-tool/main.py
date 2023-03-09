from xmlToJsonLDConverter import xmlToJsonLDConverter

parameters = {
    "companyUuid": "bd53cf0a-2e2f-4230-a591-0233290b5f9b",
    "companyName": "DIGIN",
    "isVersionOfUrl": "https://digin.no/baseprofile/",
    "documents": [
        {
            "docType": "RD",
            "docTopic": "Base Voltage",
            "docTitle": "DIGIN10-30-BaseVoltage_RD"
        },
        {
            "docType": "RD",
            "docTopic": "Geographical Region",
            "docTitle": "DIGIN10-30-GeographicalRegion_RD"
        },
        {
            "docType": "BM",
            "docTopic": "Boundry",
            "docTitle": "DIGIN10-30-HV1-MV1_BM"
        },
        {
            "docType": "AS",
            "docTopic": "Asset",
            "docTitle": "DIGIN10-30-LV1_AS"
        },
        {
            "docType": "CU",
            "docTopic": "Customer",
            "docTitle": "DIGIN10-30-LV1_CU"
        },
        {
            "docType": "DL",
            "docTopic": "Diagram Layout",
            "docTitle": "DIGIN10-30-LV1_DL"
        },
        {
            "docType": "EQ",
            "docTopic": "Equipment",
            "docTitle": "DIGIN10-30-LV1_EQ"
        },
        {
            "docType": "GL",
            "docTopic": "Geographical Location",
            "docTitle": "DIGIN10-30-LV1_GL"
        },
        {
            "docType": "OP",
            "docTopic": "Operation",
            "docTitle": "DIGIN10-30-LV1_OP"
        },
        {
            "docType": "OR",
            "docTopic": "Object Reference",
            "docTitle": "DIGIN10-30-LV1_OR"
        },
        {
            "docType": "SC",
            "docTopic": "Short Circuit",
            "docTitle": "DIGIN10-30-LV1_SC"
        },
        {
            "docType": "SSH",
            "docTopic": "Steady State Hypothesis",
            "docTitle": "DIGIN10-30-LV1_SSH"
        },
        {
            "docType": "AC",
            "docTopic": "AssetCatalogue",
            "docTitle": "DIGIN10-30-M1_AC"
        },
        {
            "docType": "RD",
            "docTopic": "Measurement Value Source",
            "docTitle": "DIGIN10-30-MeasurementValueSource_RD"
        },
        {
            "docType": "AS",
            "docTopic": "Asset",
            "docTitle": "DIGIN10-30-MV1_AS"
        },
        {
            "docType": "CU",
            "docTopic": "Customer",
            "docTitle": "DIGIN10-30-MV1_CU"
        },
        {
            "docType": "DL",
            "docTopic": "Diagram Layout",
            "docTitle": "DIGIN10-30-MV1_DL"
        },
        {
            "docType": "EQ",
            "docTopic": "Equipment",
            "docTitle": "DIGIN10-30-MV1_EQ"
        },
        {
            "docType": "GL",
            "docTopic": "Geographical Location",
            "docTitle": "DIGIN10-30-MV1_GL"
        },
        {
            "docType": "OP",
            "docTopic": "Operation",
            "docTitle": "DIGIN10-30-MV1_OP"
        },
        {
            "docType": "SC",
            "docTopic": "Short Circuit",
            "docTitle": "DIGIN10-30-MV1_SC"
        },
        {
            "docType": "SSH",
            "docTopic": "Steady State Hypothesis",
            "docTitle": "DIGIN10-30-MV1_SSH"
        },
        {
            "docType": "BM",
            "docTopic": "Boundry",
            "docTitle": "DIGIN10-30-MV1-LV1_BM"
        },
        {
            "docType": "SV",
            "docTopic": "State Variables",
            "docTitle": "DIGIN10-30-MV1-LV1_SV"
        },
        {
            "docType": "TP",
            "docTopic": "Topology",
            "docTitle": "DIGIN10-30-MV1-LV1_TP"
        },
        {
            "docType": "RD",
            "docTopic": "Reading Quality Type",
            "docTitle": "DIGIN10-30-ReadingQualityType_RD"
        },
        {
            "docType": "RD",
            "docTopic": "Reading Type",
            "docTitle": "DIGIN10-30-ReadingType_RD"
        }
    ]
}

for i in range(0, len(input["documents"])):

    companyUuid = parameters["companyUuid"]
    companyName = parameters["companyName"]
    isVersionOfUrl = parameters["isVersionOfUrl"]
    docType = parameters["documents"][i]["docType"]
    docTopic = parameters["documents"][i]["docTopic"]
    docTitle = parameters["documents"][i]["docTitle"]
    
    xmlToJsonLDConverter(companyUuid, companyName, isVersionOfUrl, docType, docTopic, docTitle)