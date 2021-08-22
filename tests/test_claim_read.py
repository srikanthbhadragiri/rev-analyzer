import xml.etree.ElementTree as ET
from io import StringIO
import xml.dom.minidom

import pandas as pd

document = """\
<slideshow>
<title>Demo slideshow</title>
<slide><title>Slide title</title>
<point>This is a demo</point>
<point>Of a program for processing slides</point>
</slide>

<slide><title>Another demo slide</title>
<point>It is important</point>
<point>To have more than</point>
<point>one slide</point>
</slide>
</slideshow>
"""

dom = xml.dom.minidom.parseString(document)
print(dom)


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

slides = dom.getElementsByTagName("slide")
print(slides)

for slide in slides:
    titles = slide.getElementsByTagName('title')
    for title in titles:
        print('Slide Title ', getText(title.childNodes))

    points = slide.getElementsByTagName('point')
    for point in points:
        print("point: ", getText(point.childNodes))

# fileName = "../xml/claim_sample.xml"
# data = minidom.parse(fileName)
#
# claims = data.getElementsByTagName("Claim")
# print(claims)
#
# encounter = claims[0].getElementsByTagName("Encounter")
# fId = encounter.getElementsByTagName("FacilityID")

# for claim in claims:
#     encounter = claim.getElementsByTagName("Encounter")
#     fId = encounter.getElementsByTagName("FacilityID")
#     pId = encounter.getElementsByTagName("PatientID")
#     print(getText(fId.childNodes))

# print(encounter)


# tagname = dat.getElementsByTagName('Claim')
# print(tagname)
# print(tagname.length)
# print(tagname[0])

# tree = ET.parse(fileName)
# root = tree.getroot()

# for child in root:
#     print(child.tag, child.attrib)

# for claim in root.findall("./Claim/"):
#     print(claim.tag, claim.text)

# for enc in root.findall("./Claim/Encounter/"):
#     print(enc.tag, enc.text)

# f = StringIO(fileName)
# context = ET.iterparse(f, events=("start", "end"))
#
# for action, elem in context:
#     print("%s: %s" % (action, elem.tag))


# ET.dump(tree)

# claimList = []
#
# for elm in root.findall('.//'):
#     print("tag: ", elm.tag, ", value: ", elm.text)
#     if elm.tag == "Claim":
#         claimDist = {elm.tag: elm.text}
#     if elm.tag == "Encounter":
#         encounterDist = {elm.tag: elm.text}

# print(claimDist)
# print(encounterDist)
