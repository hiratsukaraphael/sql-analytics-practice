
# ============================================================
# 17 - REPEATED CUSTOMERS AND REVENUE METRICS
# Product / Growth Analytics
# ============================================================

import pandas as pd

# DATASET: one row per order
df = pd.DataFrame({
    "order_id": [
        1,2,3,4,5,6,7,8,9,10
    ],
    "user_id": [
        101,102,101,103,104,
        102,105,103,105,106
    ],
    "channel": [
        "Organic", "Paid", "Organic",
        "Referral", "Paid", "Paid",
        "Organic", "Referral", "Organic", "Referral"
    ],
    "revenue": [
        40,100,60,50,150,
        80,30,70,20,90
    ]
})

print("ORIGINAL DATA")
print(df)


# TASK A - MULTIPLE METRICS

summary = df.groupby("channel").agg(
    total_revenue=("revenue", "sum"),
    orders=("order_id", "nunique"),
    customers=("user_id", "nunique")
)

print("\nGROUPED SUMMARY")
print(summary)


# TASK B - RESET INDEX

summary = summary.reset_index()

print("\nSUMMARY DATAFRAME")
print(summary)


# TASK C - REVENUE PER CUSTOMER

summary["revenue_per_customer"] = (
    summary["total_revenue"] /
    summary["customers"]
)


# TASK D - AVERAGE ORDER VALUE

summary["average_order_value"] = (
    summary["total_revenue"] /
    summary["orders"]
)


# TASK E - SORT DESCENDING

summary = summary.sort_values(
    "revenue_per_customer",
    ascending=False
)

print("\nFINAL CHANNEL RANKING")
print(summary.round(2))


# VALIDATION

assert len(df) == 10
assert df["user_id"].nunique() == 6

assert summary.iloc[0]["channel"] == "Paid"
assert summary.iloc[0]["total_revenue"] == 330
assert summary.iloc[0]["customers"] == 2

assert summary.loc[
    summary["channel"] == "Organic",
    "average_order_value"
].iloc[0] == 37.5

print("\nAll checks passed.")


# BUSINESS INTERPRETATION
#
# Paid:
#   Revenue/customer = $165
#   Average order value = $110
#
# Referral:
#   Revenue/customer = $105
#   Average order value = $70
#
# Organic:
#   Revenue/customer = $75
#   Average order value = $37.50
#
# This order-level dataset includes purchasers
# only. To calculate revenue per acquired user,
# include non-purchasing customers from the
# acquisition/customer table as well.
