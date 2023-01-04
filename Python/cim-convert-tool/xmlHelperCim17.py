import xml.etree.ElementTree as ET

def textImport(CIMClass, tag):
    if CIMClass.find(tag) == None:
        return None
    else:
        return CIMClass.find(tag).text

def attributeImport(CIMClass, tag, attribute):
    if CIMClass.find(tag) == None:
        return None
    else:
        return CIMClass.find(tag).get(attribute)

def textExport(element, CIMClass, tagname):
    if element !=None:
        ET.SubElement(CIMClass, tagname).text = element

def attributeExport(element, CIMClass, tagname, attributeName):
    if element !=None:
        ET.SubElement(CIMClass, tagname).set(attributeName, element)

def prefixListReplacer(tags, cimPrefix, euPrefix, rdfPrefix, mdPrefix):
    outputtags = []
    for i in range(0, len(tags)):
        if tags[i].startswith('cim:'):
            outputtags.append(tags[i].replace('cim:', '{' + cimPrefix + '}'))
        elif tags[i].startswith('eu:'):
            outputtags.append(tags[i].replace('eu:', '{' + euPrefix + '}'))
        elif tags[i].startswith('rdf:'):
            outputtags.append(tags[i].replace('rdf:', '{' + rdfPrefix + '}'))
        elif tags[i].startswith('md:'):
            outputtags.append(tags[i].replace('md:', '{' + mdPrefix + '}'))
    return outputtags

def prefixTagReplacer(tag, cimPrefix, euPrefix, rdfPrefix, mdPrefix):
    if tag.startswith('cim:'):
        return tag.replace('cim:', '{' + cimPrefix + '}')
    elif tag.startswith('eu:'):
        return tag.replace('eu:', '{' + euPrefix + '}')
    elif tag.startswith('rdf:'):
        return tag.replace('rdf:', '{' + rdfPrefix + '}')
    elif tag.startswith('md:'):
        return tag.replace('md:', '{' + mdPrefix + '}')

def valueDataTypeConverter(value, type):
    if type == 'bool' and value == 'true':
        return True
    if type == 'bool' and value == 'false':
        return False
    elif type == 'float':
        return float(value)
    elif type == 'int':
        return int(value)
    elif type == 'string':
        return value

def valueDataTypeConverter(value, type):
    if type == 'bool' and value == 'true':
        return True
    if type == 'bool' and value == 'false':
        return False
    elif type == 'float':
        return float(value)
    elif type == 'int':
        return int(value)
    elif type == 'string':
        return value

def textsXmlToJsonLdConverter(object, key, value, valueType):
    if value != None:
        if key != 'cim:IdentifiedObject.mRID':
            object[key] = valueDataTypeConverter(value, valueType)

def refsXmlToJsonLdConverter(object, key, value):
    if value != None:
        object[key] = {'@id': value.replace('#_', 'urn:uuid:')}