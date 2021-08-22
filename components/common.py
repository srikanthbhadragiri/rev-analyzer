import datetime
import components.create_db as db

# claimFileName = "MF1397_A001_2021-03-31_IS015009.xml"
# remittanceFile = "MF1397-13252993-11318696-30042021120439.XML"

REMITTANCE_ADVICE = "Remittance.Advice"
CLAIM_SUBMISSION = "Claim.Submission"
CLAIM_RESUBMISSION = "Claim.Resubmission"

def getTextValue(node, child):
    if node.getElementsByTagName(child):
        if node.getElementsByTagName(child)[0].firstChild is not None:
            return node.getElementsByTagName(child)[0].firstChild.nodeValue


def getTimeValue(node, child):
    if node.getElementsByTagName(child):
        if node.getElementsByTagName(child)[0].firstChild is not None:
            value = node.getElementsByTagName(child)[0].firstChild.nodeValue
            return str(datetime.datetime.strptime(value, "%d/%m/%Y %H:%M"))

def getDBConn() -> object:
    conn = db.establishConn()
    if db.verifyConnection(conn):
        print("DB connection successful!")
        return conn
    else:
        print("DB connection not successful!")
        return None

