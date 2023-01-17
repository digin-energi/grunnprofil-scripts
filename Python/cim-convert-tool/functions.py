import xml.etree.ElementTree as ET

def xmlPrefixListReplacer(tags, cimPrefix, euPrefix, rdfPrefix, mdPrefix):
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