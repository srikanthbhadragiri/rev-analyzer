
claimslist = [('{CLD110616,CLD110619,CLD110621,CLD110604,CLD110682,CLD110600,CLD110622,CLD110677,CLD110692}',), ('{CLD110418,CLD110349}',)]


def findClm(claimid):
    for claims in claimslist:
        for cid in claims:
            print('$$$$ ', cid, claimid)
            print(type(cid), type(claimid))
            if cid.find(claimid) != -1:
                print('item found', claimid)
                return True
    return False


tofindClm = 'CLD110604'

print(findClm(tofindClm))


# str1 = '{CLD110616,CLD110619,CLD110621,CLD110604,CLD110682,CLD110600,CLD110622,CLD110677,CLD110692}'
# str2 = 'CLD110604XX'
#
# print(str1.find(str2))