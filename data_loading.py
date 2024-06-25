import json
import pandas as pd

def load_data():
    with open('/mnt/data/business_primary_tradelines.json', 'r') as file:
        business_tradelines = json.load(file)

    with open('/mnt/data/consumer_primary_tradelines.json', 'r') as file:
        consumer_tradelines = json.load(file)

    au_inventory_df = pd.read_csv('/mnt/data/authorized_user_card_inventory_SKU.csv')
    au_inventory = au_inventory_df.to_dict(orient='records')

    business_loan_approval_data = pd.read_csv('/mnt/data/Business Loan Approval Data.csv').dropna(how="all")
    personal_loan_approval_data = pd.read_csv('/mnt/data/Personal Loan Approval Amounts by FICO Score.csv').dropna(how="all")

    return business_tradelines, consumer_tradelines, au_inventory, business_loan_approval_data, personal_loan_approval_data
