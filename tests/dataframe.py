# ('CLD113375', datetime.datetime(2021, 3, 31, 10, 20), Decimal('169.00'), '0', Decimal('169.00'))
# ('CLD113459', datetime.datetime(2021, 3, 31, 10, 20), Decimal('56.00'), '10', Decimal('46.00'))
#
#
# Claim id || Submission Date || Gross || PShare || Net || Remittance Id || Submission Date ||
import pandas as pd

reportA001 = [{"claim_id": 1212121,
               "activities": [{"id": "abcd", "net": 10.00, "paidAmt": 10.00, "denial_code": "null"},
                              {"id": "abcd", "net": 10.00, "paidAmt": 10.00, "denial_code": "null"},
                              {"id": "abcd", "net": 10.00, "paidAmt": 10.00, "denial_code": "null"}]},
              {"claim_id": 2323232,
               "activities": [{"id": "abcd", "net": 10.00, "paidAmt": 10.00, "denial_code": "null"},
                              {"id": "abcd", "net": 10.00, "paidAmt": 10.00, "denial_code": "null"},
                              {"id": "abcd", "net": 10.00, "paidAmt": 10.00, "denial_code": "null"}]}
              ]
print(type(reportA001))

# reportA001Df = pd.DataFrame(reportA001)
# print(type(reportA001Df))
# print(reportA001Df)
# print(reportA001Df.describe())


repA001 = \
    [{"claim_id": 1212121, "act_id": "abcd", "act_net": 10.00, "act_paidAmt": 10.00, "act_denial_code": "null"},
     {"claim_id": 1212121, "act_id": "abcd", "act_net": 10.00, "act_paidAmt": 10.00, "act_denial_code": "null"},
     {"claim_id": 1212121, "act_id": "abcd", "act_net": 10.00, "act_paidAmt": 10.00, "act_denial_code": "null"},
     {"claim_id": 2323232, "act_id": "abcd", "act_net": 10.00, "act_paidAmt": 10.00, "act_denial_code": "null"},
     {"claim_id": 2323232, "act_id": "abcd", "act_net": 10.00, "act_paidAmt": 10.00, "act_denial_code": "null"},
     {"claim_id": 2323232, "act_id": "abcd", "act_net": 10.00, "act_paidAmt": 10.00, "act_denial_code": "null"},
     {"claim_id": 2323232, "act_id": "abcd", "act_net": 10.00, "act_paidAmt": 10.00, "act_denial_code": "null"}
    ]

print(type(repA001))

repdf = pd.DataFrame(repA001)
print(type(repdf))