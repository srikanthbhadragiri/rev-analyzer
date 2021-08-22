def ifFileNameExists(conn, filename):
    if conn:
        cursor = conn.cursor()
        # filename = 'MF1397_A001_2021-03-31_IS015009.xml'
        queryStr = "SELECT * FROM claim_file_details WHERE file_name = '" + filename + "'"
        print("queryStr : ", queryStr)
        cursor.execute(queryStr)
        result = cursor.fetchall();
        if len(result) > 0:
            return True
        else:
            return False


def allClaimIds(conn):
    if conn:
        cursor = conn.cursor()
        queryStr = """SELECT claim_ids FROM claim_file_details WHERE claim_type = 'Submission'"""
        cursor.execute(queryStr)
        result = cursor.fetchall();
        return result


def allA001ClaimsMarch(conn):
    if conn:
        cursor = conn.cursor()
        queryStr = """
        SELECT claim_id, submission_date, gross, patientshare, net 
        FROM claim_master 
        where receiver_id = 'A001' 
        AND EXTRACT(MONTH FROM submission_date) = 3"""
        cursor.execute(queryStr)
        result = cursor.fetchall()
        return result


def getA001ResubClaims(conn, claimsStr):
    # print("in resub clains ", claimsStr)
    if conn:
        cursor = conn.cursor()
        queryStr = "SELECT claim_id, submission_date, gross, patientshare, net, Resub_Type, Resub_Comment FROM resub_master WHERE claim_id in ("+claimsStr+") "
        cursor.execute(queryStr)
        result = cursor.fetchall()
        # print('result ', result[0])
        return result
