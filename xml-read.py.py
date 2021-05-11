import xml.etree.ElementTree as ET
import json
import os

path = './' # you can give your path
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    print(fullname)
    #here just pass the file name dynamically under parse function
    #tree = ET.parse('20210503_Sample_FreddieImagineResponse.xml')
    tree = ET.parse(fullname)
    root = tree.getroot()
    dict1={}

    # one specific item attribute
    print('Item #2 attribute:')
    print(root[0])
    for i in root[0]:
        #print(i.tag)
        if i.tag=='MILenderIdentifier':
            dict1['MILenderIdentifier']=i.text
        elif i.tag=='EventType':
            dict1['EventType']=i.text
        elif i.tag=='EventId':
            dict1['EventId']=i.text
        elif i.tag=='MIVersion':
            dict1['MIVersion']=i.text
    print(dict1)
    #json.dumps(dict1)
    res={key:val.replace('"', '') for key, val in dict1.items()}
    fileName=res['MILenderIdentifier']+'-'+res['EventType']+'-'+res['EventId']+'-'+res['MIVersion']+'.xml'
    print(fileName)