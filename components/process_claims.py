from typing import List, Any, Union

import components.common as cm


def processHeader(dom, filename):
    print('process claims', filename)
    header = dom.getElementsByTagName("Header")
    header_dict = {"FileName": filename, "ClaimType": "Submission"}
    for head in header:
        header_dict["SenderID"] = cm.getTextValue(head, 'SenderID')
        header_dict["ReceiverID"] = cm.getTextValue(head, 'ReceiverID')
        header_dict["RecordCount"] = cm.getTextValue(head, 'RecordCount')
        header_dict["TransactionDate"] = cm.getTimeValue(head, 'TransactionDate')
        header_dict["DispositionFlag"] = cm.getTextValue(head, 'DispositionFlag')
        header_dict["RecordCount"] = cm.getTextValue(head, 'RecordCount')

    return header_dict


# claimsList = []
# claimIDsList = []


def processClaims(dom):
    claimsList = []
    claim_dict = {}
    diag_dict = {}
    acti_dict = {}
    obs_dict = {}
    diag_list = []
    acti_list = []
    obs_list = []
    for claim in dom.getElementsByTagName("Claim"):
        claim_dict["ClaimID"] = cm.getTextValue(claim, 'ID')
        claim_dict["IDPayer"] = cm.getTextValue(claim, 'IDPayer')
        claim_dict["MemberID"] = cm.getTextValue(claim, 'MemberID')
        claim_dict["PayerID"] = cm.getTextValue(claim, 'PayerID')
        claim_dict["ProviderID"] = cm.getTextValue(claim, 'ProviderID')
        claim_dict["EmiratesIDNumber"] = cm.getTextValue(claim, 'EmiratesIDNumber')
        claim_dict["Gross"] = cm.getTextValue(claim, 'Gross')
        claim_dict["PatientShare"] = cm.getTextValue(claim, 'PatientShare')
        claim_dict["Net"] = cm.getTextValue(claim, 'Net')
        claim_dict["VAT"] = cm.getTextValue(claim, 'VAT')

        for enc in claim.getElementsByTagName('Encounter'):
            claim_dict["FacilityID"] = cm.getTextValue(enc, 'FacilityID')
            claim_dict["FacilityType"] = cm.getTextValue(enc, 'Type')
            claim_dict["PatientID"] = cm.getTextValue(enc, 'PatientID')
            claim_dict["Start"] = cm.getTimeValue(enc, 'Start')
            claim_dict["End"] = cm.getTimeValue(enc, 'End')
            claim_dict["StartType"] = cm.getTextValue(enc, 'StartType')
            claim_dict["EndType"] = cm.getTextValue(enc, 'EndType')

        for diag in claim.getElementsByTagName('Diagnosis'):
            diag_dict["ClaimID"] = claim_dict["ClaimID"]
            diag_dict["Type"] = cm.getTextValue(diag, 'Type')
            diag_dict["Code"] = cm.getTextValue(diag, 'Code')
            diag_list.append(diag_dict)
            diag_dict = {}

        for acti in claim.getElementsByTagName('Activity'):
            acti_dict["ClaimID"] = claim_dict["ClaimID"]
            acti_dict["ID"] = cm.getTextValue(acti, 'ID')
            acti_dict["Start"] = cm.getTimeValue(acti, 'Start')
            acti_dict["Type"] = cm.getTextValue(acti, 'Type')
            acti_dict["Quantity"] = cm.getTextValue(acti, 'Quantity')
            acti_dict["Code"] = cm.getTextValue(acti, 'Code')
            acti_dict["Net"] = cm.getTextValue(acti, 'Net')
            acti_dict["OrderingClinician"] = cm.getTextValue(acti, 'OrderingClinician')
            acti_dict["Clinician"] = cm.getTextValue(acti, 'Clinician')
            acti_dict["PriorAuthorizationID"] = cm.getTextValue(acti, 'PriorAuthorizationID')
            acti_dict["VAT"] = cm.getTextValue(acti, 'VAT')
            acti_dict["VATPercent"] = cm.getTextValue(acti, 'VATPercent')

            for obs in acti.getElementsByTagName('Observation'):
                obs_dict["ClaimID"] = acti_dict["ClaimID"]
                obs_dict["ID"] = acti_dict["ID"]
                obs_dict["Type"] = cm.getTextValue(obs, 'Type')
                obs_dict["Code"] = cm.getTextValue(obs, 'Code')
                obs_dict["Value"] = cm.getTextValue(obs, 'Value')
                # if obs_dict["Value"] is None:
                #     obs_dict["Value"] = "0"
                obs_dict["Value"] = cm.getTextValue(obs, 'Value')
                obs_dict["ValueType"] = cm.getTextValue(obs, 'ValueType')
                obs_list.append(obs_dict)
                obs_dict = {}

            acti_dict["Observations"] = obs_list
            acti_list.append(acti_dict)
            obs_list = []
            acti_dict = {}

        if claim.getElementsByTagName('Resubmission'):
            resub = claim.getElementsByTagName('Resubmission')[0]
            print('resub ', resub)
            print("This is a resubmission claim - ", claim_dict["ClaimID"])
            claim_dict["ClaimType"] = "Resubmission"
            claim_dict["ResubType"] = cm.getTextValue(resub, 'Type')
            claim_dict['ResubComment'] = cm.getTextValue(resub, 'Comment')
            print("Resubmit details : ", claim_dict["ResubType"], claim_dict['ResubComment'])
        else:
            print("This is a claim submission - ", claim_dict["ClaimID"])
            claim_dict["ClaimType"] = "Submission"

        claim = {"claim": claim_dict, "diagnosis": diag_list, "activity": acti_list}
        diag_list = []
        acti_list = []
        claimsList.append(claim)
        # claimIDsList = []
        claim_dict = {}
        diag_dict = {}
        acti_dict = {}

    return claimsList
