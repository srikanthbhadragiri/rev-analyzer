import components.common as cm
import components.validate_data as vd

# remitList = []
# remitClaimIDsList = []
db_conn = cm.getDBConn()


def processRemitHeader(dom, filename):
    header = dom.getElementsByTagName("Header")
    header_dict = {"FileName": filename, "ClaimType": "Remittance"}
    for head in header:
        header_dict["SenderID"] = cm.getTextValue(head, 'SenderID')
        header_dict["ReceiverID"] = cm.getTextValue(head, 'ReceiverID')
        header_dict["RecordCount"] = cm.getTextValue(head, 'RecordCount')
        header_dict["TransactionDate"] = cm.getTimeValue(head, 'TransactionDate')
        header_dict["DispositionFlag"] = cm.getTextValue(head, 'DispositionFlag')

    return header_dict


def getAllClaimIds():
    print('get all claims --- ')
    claimsList = vd.allClaimIds(db_conn)
    print('all claims ', claimsList)
    print(type(claimsList))
    return claimsList
    # print([item for item in claimsList if 'CLD113436' in item])

# This function should be invoked when a remittance claim has to be processed.
# This function will check if the claim exists in db.
# If claim exists, only then the remittance has to be processed. else move to the next claim in the file.
# MF1397_791712_172.3_MF1397_A002_2021-05-07_IS015621_79.xml

def claimIdExists(claimid, claimslist):
    print('claimslist ', claimslist)
    for claims in claimslist:
        for cid in claims:
            if cid.find(claimid) != -1:
                print('Claim found in DB ', claimid)
                return True
    print('Claim Not found: ', claimid)
    return False


def processRemit(dom):
    remitList = []
    remit_dict = {}
    act_dict = {}
    act_list = []
    allClaimsIds = getAllClaimIds()

    for claim in dom.getElementsByTagName("Claim"):
        # check if claim id exists in db
        claimId = cm.getTextValue(claim, 'ID')
        if claimIdExists(claimId, allClaimsIds):
            print('processing claim ', claimId)
            remit_dict["ClaimID"] = cm.getTextValue(claim, 'ID')
            # remitClaimIDsList.append(remit_dict["ClaimID"])
            remit_dict["IDPayer"] = cm.getTextValue(claim, 'IDPayer')
            remit_dict["ProviderID"] = cm.getTextValue(claim, 'ProviderID')
            remit_dict["PaymentReference"] = cm.getTextValue(claim, 'PaymentReference')
            remit_dict["DateSettlement"] = cm.getTimeValue(claim, 'DateSettlement')

            for enc in claim.getElementsByTagName('Encounter'):
                remit_dict["FacilityID"] = cm.getTextValue(enc, 'FacilityID')
                # print(remit_dict)
            for act in claim.getElementsByTagName('Activity'):
                act_dict["ID"] = cm.getTextValue(act, 'ID')
                act_dict["ClaimID"] = remit_dict["ClaimID"]
                act_dict["Start"] = cm.getTimeValue(act, 'Start')
                act_dict["Type"] = cm.getTextValue(act, 'Type')
                act_dict["Quantity"] = cm.getTextValue(act, 'Quantity')
                act_dict["Code"] = cm.getTextValue(act, 'Code')
                act_dict["Net"] = cm.getTextValue(act, 'Net')
                act_dict["OrderingClinician"] = cm.getTextValue(act, 'OrderingClinician')
                act_dict["Clinician"] = cm.getTextValue(act, 'Clinician')
                act_dict["PaymentAmount"] = cm.getTextValue(act, 'PaymentAmount')
                act_dict["DenialCode"] = cm.getTextValue(act, 'DenialCode')

                act_list.append(act_dict)
                act_dict = {}

            remit = {"claim": remit_dict, "activity": act_list}
            remitList.append(remit)
            act_list = []
            remit_dict = {}
            act_dict = {}

    return remitList
