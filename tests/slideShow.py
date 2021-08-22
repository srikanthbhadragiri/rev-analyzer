import xml.dom.minidom

fileName = "../xml/slide.xml"
dom = xml.dom.minidom.parse(fileName)

# print(dom)


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


slides = dom.getElementsByTagName("slide")
print(slides)

# pt1 = slides[0].getElementsByTagName("point")
# print('pt1[0] value: ', getText(pt1[0].childNodes))
# print('pt1[1] value: ', getText(pt1[1].childNodes))
#
# pt2 = slides[1].getElementsByTagName("point")
# print('pt2[0] value: ', getText(pt2[0].childNodes))
# print('pt2[1] value: ', getText(pt2[1].childNodes))
# print('pt2[2] value: ', getText(pt2[2].childNodes))

for slide in slides:
    print(slide)
    points = slide.getElementsByTagName("point")
    print(points)
