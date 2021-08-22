import xml.dom.minidom
import components.common as cm
import components.process_claims as pc
import components.process_remittance as rc


def getTypeofClaim(filepath):
    print('filepath ' + filepath)
    xmlObj = xml.dom.minidom.parse(filepath)
    print(xmlObj)
    print('doc ele ', xmlObj.documentElement.tagName)
    if xmlObj.documentElement.tagName == cm.REMITTANCE_ADVICE:
        return cm.REMITTANCE_ADVICE
    elif xmlObj.documentElement.tagName == cm.CLAIM_SUBMISSION:
        return cm.CLAIM_SUBMISSION
    # xmlObj.documentElement.tagName == "Claim.Submission"
    # assert xmlObj.documentElement.tagName == "Claim.Submission"


def getClaimObj(filepath):
    return xml.dom.minidom.parse(filepath)


def getClaimHeaderData(filepath):
    claimsDomObj = getClaimObj(filepath)
    claim_header_data = pc.processHeader(claimsDomObj, filepath[filepath.rindex("/") + 1:])
    # claim_header_data["Claims"] = pc.claimIDsList
    return claim_header_data


def getClaimData(filepath):
    claimsDomObj = getClaimObj(filepath)
    claims_data = pc.processClaims(claimsDomObj)
    return claims_data


def getRemittanceHeaderData(filepath):
    remitDomObj = getClaimObj(filepath)
    remit_header_data = rc.processRemitHeader(remitDomObj, filepath[filepath.rindex("/") + 1:])
    # remit_header_data["claims"] = rc.remitClaimIDsList
    return remit_header_data


def getRemitData(filepath):
    remitDomObj = getClaimObj(filepath)
    remit_data = rc.processRemit(remitDomObj)
    return remit_data

# print("remit_data : ", remit_data)

# print('Header : ', header_data)
# print('Claims : ', claims_data)

# for disFlag in dispositionFlag:
#     header_dict["DispositionFlag"] = getText(disFlag.childNodes)

# def getText(nodelist):
#     rc = []
#     for node in nodelist:
#         if node.nodeType == node.TEXT_NODE:
#             rc.append(node.data)
#     return ''.join(rc)
