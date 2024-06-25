def generate_header(title, subtitle):
    header = f"""
    ====================================
    {title}
    ====================================
    {subtitle}
    ------------------------------------
    """
    return header

def generate_report(client_name, company_name, user_name, date, personal_profile, business_profile, good_df, better_df, best_df, funding_capacity_personal, funding_capacity_business):
    title = "FUNDABILITY REPORT"
    subtitle = "Personal and Business Credit Analysis and Recommendations"
    report = generate_header(title, subtitle)
    
    # Add Gap Analysis to Report
    report += f"""
    {generate_header("Gap Analysis", "Personal Credit Profile")}
    Factor    Current Value    Target Value    Gap Identified
    Credit Utilization    {personal_profile['credit_utilization']}%    < 10%    Reduce utilization
    Payment History    {personal_profile['payment_history']}    100% on-time payments    {personal_profile['payment_gap']}
    Average Account Age    {personal_profile['average_account_age']} years    7-10 years    Increase account age
    Oldest Account Age    {personal_profile['oldest_account_age']} years    ≥ 15 years    Increase oldest age
    Public Records and Inquiries    {personal_profile['public_records']} inquiries    No public records    Avoid inquiries
    New Credit Inquiries    {personal_profile['new_credit_inquiries']} inquiries    ≤ 2 per year    Reduce inquiries
    Credit Mix    {personal_profile['credit_mix']}    Diverse mix    Enhance credit mix
    
    {generate_header("Gap Analysis", "Business Credit Profile")}
    Factor    Current Value    Target Value    Gap Identified
    Payment History    {business_profile['payment_history']}    100% on-time payments    Maintain
    Credit Utilization    {business_profile['credit_utilization']}%    < 30%    Reduce utilization
    Age of Credit Accounts    {business_profile['age_of_credit_accounts']} years    ≥ 5 years    Maintain
    Business Age    {business_profile['business_age']} year    ≥ 10 years    Increase business age
    Credit Mix    {business_profile['credit_mix']}    Diverse mix    Enhance credit mix
    Public Records and Inquiries    N/A    No public records    Maintain
    
    {generate_header("Calculate Fundability Scores", "Personal Credit")}
    Factor    Score    Weight    Weighted Score
    Payment History    0    35%    0.0
    Amounts Owed    5    30%    1.5
    Length of Credit History     7    15%    1.05
    Credit Mix     7    10%    0.7
    New Credit     0    10%    0.0
    Estimated Funding Capacity    ${funding_capacity_personal}
    
    {generate_header("Calculate Fundability Scores", "Business Credit")}
    Factor    Score    Weight    Weighted Score
    Payment History     5    35%    1.75
    Credit Utilization     3    30%    0.9
    Age of Credit Accounts     7    15%    1.05
    Business Age     0    10%    0.0
    Credit Mix     3    5%    0.15
    Public Records and Inquiries     5    5%    0.25
    Estimated Funding Capacity    ${funding_capacity_business}
    
    {generate_header("Tradeline Recommendations", "Good Level Recommendations")}
    {good_df.to_string(index=False)}
    Total Investment: ${calculate_total_investment(good_recommendations)}
    Summary: {summary_good}
    
    {generate_header("Tradeline Recommendations", "Better Level Recommendations")}
    {better_df.to_string(index=False)}
    Total Investment: ${calculate_total_investment(better_recommendations)}
    Summary: {summary_better}
    
    {generate_header("Tradeline Recommendations", "Best Level Recommendations")}
    {best_df.to_string(index=False)}
    Total Investment: ${calculate_total_investment(best_recommendations)}
    Summary: {summary_best}
    
    {generate_header("Comparison with Desired Funding", "")}
    Level    Fundability Score    Estimated Funding Capacity    Desired Funding    Total Investment
    Good    {personal_score}    ${funding_capacity_personal}    $60,000    ${calculate_total_investment(good_recommendations)}
    Better    {personal_score}    ${funding_capacity_personal}    $60,000    ${calculate_total_investment(better_recommendations)}
    Best    {personal_score}    ${funding_capacity_personal}    $60,000    ${calculate_total_investment(best_recommendations)}
    
    END OF THIS REPORT - THANK YOU FOR YOUR BUSINESS
    {client_name}
    {company_name}
    Date: {date}
    
    Generate another report? (Y/N)
    """
    
    print(report)
