# kpi_metrics.py
# Refined Python script to calculate lead conversion metrics using pandas

import pandas as pd

# Simulated CRM export
data = {
    "lead_id": [1, 2, 3, 4, 5, 6, 7],
    "status": ["MQL", "SQL", "Closed", "MQL", "Closed", "SQL", "Closed"],
    "campaign": ["A", "A", "B", "A", "B", "C", "A"]
}

df = pd.DataFrame(data)

# Define qualified leads as MQL + SQL
qualified_leads = df[df["status"].isin(["MQL", "SQL"])]
closed_deals = df[df["status"] == "Closed"]

# Calculate conversion rate from qualified to closed
conversion_rate = len(closed_deals) / len(qualified_leads) * 100
print(f"Qualified-to-Closed Conversion Rate: {conversion_rate:.2f}%")

# Campaign performance analysis
campaign_performance = df[df["status"] == "Closed"].groupby("campaign").size()
print("\nClosed deals by campaign:")
print(campaign_performance)
