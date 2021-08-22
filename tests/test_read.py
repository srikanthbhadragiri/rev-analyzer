import xml.etree.ElementTree as ET
import pandas as pd
import psycopg2
import time
import datetime

# <?xml version="1.0"?>
# <data>
#     <country name="Liechtenstein">
#         <rank updated="yes">2</rank>
#         <year>2008</year>
#         <gdppc>141100</gdppc>
#         <neighbor name="Austria" direction="E"/>
#         <neighbor name="Switzerland" direction="W"/>
#     </country>
#     <country name="Singapore">
#         <rank updated="yes">5</rank>
#         <year>2011</year>
#         <gdppc>59900</gdppc>
#         <neighbor name="Malaysia" direction="N"/>
#     </country>
#     <country name="Panama">
#         <rank updated="yes">69</rank>
#         <year>2011</year>
#         <gdppc>13600</gdppc>
#         <neighbor name="Costa Rica" direction="W"/>
#         <neighbor name="Colombia" direction="E"/>
#     </country>
# </data>


fileName = "../xml/claim_sample.xml";

tree = ET.parse(fileName)
root = tree.getroot()

# working search
# for elm in root.findall('.//'):      # .// lists all the tags in the xml
#     print('Tag: ',elm.tag, ",  Value: ", elm.text)

# L = ["claim1", "claim2"]
# print(type(L))
#
# S = {"Claim"}
# print(type(S))
#
# D = {"Claim": "09090"}
# print(type(D))
#
# claimItems = [{"Id": "CLD113375", "MemberID": "07404956"}]
# print(type(claimItems))
#
# claimDict = {"claim": claimItems}
# print(claimDict)

# List of nested dictionary initialization
claimList = [
    {
        "Claim": [{"Id": "CLD113375", "MemberID": "07404956"}],
        "Encounter": [{"FacilityID": "MF1397", "PatientID": "OPLUS025436"}],
        "Diagnosis": [{"Type": "Principal", "Code": "N47.1"}],
        "Activity": [{"ID": "A-CH332201", "Start": "28/03/2021 13:41"},
                     {"ID": "A-CH332201", "Start": "28/03/2021 13:41"},
                     {"ID": "A-CH332201", "Start": "28/03/2021 13:41"}],
    },
    {
        "Claim": [{"Id": "CLD113459", "MemberID": "10587189"}],
        "Encounter": [{"FacilityID": "MF1397", "PatientID": "OPLUS025141"}],
        "Diagnosis": [{"Type": "Principal", "Code": "N47.1"},
                      {"Type": "Principal", "Code": "N47.1"},
                      {"Type": "Principal", "Code": "N47.1"}],
        "Activity": [{"ID": "A-CH332201", "Start": "28/03/2021 13:41"},
                     {"ID": "A-CH332201", "Start": "28/03/2021 13:41"}],
    }
]

print('claimList ', claimList)
print(' ---- ', type(claimList))

# rows list initialization
rows = []

# appending rows
for data in claimList:
    data_row = data['Claim']
    encounter = data['Encounter']
    diagnosis = data['Diagnosis']
    activity = data['Activity']

    for row in data_row:
        row['Encounter'] = encounter
        row['Diagnosis'] = diagnosis
        row['Activity'] = activity
        rows.append(row)

# using data frame
df = pd.DataFrame(rows)
print(df)

# for elm in root.findall('.claim'):      # .// lists all the tags in the xml
#     print('Tag: ', elm.tag, ",  Value: ", elm.text)

# ET.dump(tree)     # prints the whole xml

# for elm in root.findall('.'):      # . prints the first element i.e data
#     print(elm.tag)

# for elm in root.findall('./'):      # ./ prints all the country elements
#     print(elm.tag)

# for elm in root.findall('./Claim'):      # ./country elm.attrib prints all the attributes
#     print(elm.tag)

# for elm in root.findall('.//'):      # .// lists all the tags in the xml
#     print(elm.tag, ": value ", elm.text)

# def Read_Claim(Claim):
#     for cla in root.iter('Claim'):
#         cla_dict = cla.attrib.copy()
#         # print(type(mov_dict), mov_dict)
#         cla_dict.update(cla.attrib)
#         for feature in cla:
#             if feature.tag != "Diagnosis" and feature.tag != "Activity" and feature.tag != "Encounter":
#                 cla_dict[feature.tag] = feature.text
#             if feature.tag == "Encounter":
#                 SubElement
#         yield cla_dict
#         # print(cla_dict)
#
#
# cla_df = pd.DataFrame(list(Read_Claim(root.iter('Claim'))))
# print(cla_df)
