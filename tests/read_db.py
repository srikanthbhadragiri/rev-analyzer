from typing import Union, Iterator

import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:root@127.0.0.1:5432/MoviesDB")

query1 = """SELECT 
            file_name, claim_type 
           FROM 
            claim_file_details
           WHERE claim_type = 'Claim' """

query2 = """SELECT
            DISTINCT receiver_id
            FROM claim_master"""

data = pd.read_sql(query2, engine)


query3 = """
SELECT 
    claim_master.claim_id, claim_master.member_id, claim_master.gross, 
    claim_master.net, claim_master.vat
FROM claim_master
    JOIN claim_diagnosis
    ON claim_master.claim_id = claim_diagnosis.claim_id
"""

data3 = pd.read_sql(query3, engine)
print( data3 )

# print(data)

