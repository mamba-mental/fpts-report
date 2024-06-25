import json
import pandas as pd
import sys
from data_loading import load_data
from credit_analysis import analyze_personal_credit, analyze_business_credit
from recommendations import recommend_personal_tradelines, recommend_business_tradelines, recommend_au_accounts, generate_recommendation_grid
from report_generation import generate_report

def main(client_name, company_name, user_name, date):
    with open('personal_profile.json', 'r') as f:
        personal_profile = json.load(f)
    with open('business_profile.json', 'r') as f:
        business_profile = json.load(f)

    business_tradelines, consumer_tradelines, au_inventory, business_loan_approval_data, personal_loan_approval_data = load_data()

    personal_credit_targets = {
        "credit_utilization": "< 10%",
        "payment_history": "100% on-time payments",
        "average_account_age": "7-10 years",
        "oldest_account_age": "≥ 15 years",
        "public_records": "No public records",
        "new_credit_inquiries": "≤ 2 per year",
        "credit_mix": "Diverse mix"
    }

    business_credit_targets = {
        "payment_history": "100% on-time payments",
        "credit_utilization": "< 30%",
        "age_of_credit_accounts": "≥ 5 years",
        "business_age": "≥ 10 years",
        "credit_mix": "Diverse mix",
        "public_records": "No public records"
    }

    analyze_personal_credit(personal_profile, personal_credit_targets)
    analyze_business_credit(business_profile, business_credit_targets)

    good_recommendations = recommend_personal_tradelines(personal_profile, consumer_tradelines)
    better_recommendations = recommend_business_tradelines(business_profile, business_tradelines)
    best_recommendations, new_utilization, new_credit_score, new_funding_capacity = recommend_au_accounts(personal_profile, au_inventory, 5)

    good_df = pd.DataFrame(good_recommendations)
    better_df = pd.DataFrame(better_recommendations)
    best_df = pd.DataFrame(best_recommendations)

    funding_capacity_personal = 0  # Calculate based on personal_score and targets
    funding_capacity_business = 0  # Calculate based on business_score and targets

    generate_report(client_name, company_name, user_name, date, personal_profile, business_profile, good_df, better_df, best_df, funding_capacity_personal, funding_capacity_business)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python main.py <client_name> <company_name> <user_name> <date>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
