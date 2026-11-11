
# ============================================================
# 12 - ISIN AND CHANNEL SEGMENTATION
#
# Skills:
# isin(), Boolean filtering, groupby(), sum(),
# sort_values(), Series vs DataFrame
# ============================================================

import pandas as pd

# 1. DATASET

df = pd.DataFrame({
    "user_id": [
        101,102,103,104,105,
        106,107,108,109,110
    ],
    "channel": [
        "Organic", "Paid Search", "Referral",
        "Organic", "Email", "Paid Search",
        "Referral", "Organic", "Email", "Paid Search"
    ],
    "revenue": [
        0,120,40,30,50,
        0,80,60,20,200
    ],
    "active": [
        1,1,1,0,1,
        0,1,1,0,1
    ]
})

print("ORIGINAL DATA")
print(df)


# TASK A - FILTER ORGANIC AND REFERRAL

selected = df[
    df["channel"].isin(["Organic", "Referral"])
]

print("\nSELECTED CHANNELS")
print(selected)


# TASK B - COUNT SELECTED USERS

selected_count = len(selected)

print("\nSELECTED USERS")
print(selected_count)


# TASK C - TOTAL SELECTED REVENUE

selected_revenue = selected["revenue"].sum()

print("\nSELECTED REVENUE")
print(selected_revenue)


# TASK D - ACTIVE USERS IN SELECTED CHANNELS

active_selected = df[
    (df["channel"].isin(["Organic", "Referral"])) &
    (df["active"] == 1)
]

print("\nACTIVE SELECTED USERS")
print(active_selected)


# TASK E - REVENUE BY CHANNEL, SORTED

active_revenue = (
    active_selected.groupby("channel")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nACTIVE REVENUE BY CHANNEL")
print(active_revenue)


# VALIDATION

assert selected_count == 5
assert selected_revenue == 210
assert len(active_selected) == 4
assert active_revenue["Referral"] == 120
assert active_revenue["Organic"] == 60

print("\nAll checks passed.")


# BUSINESS INTERPRETATION
#
# Organic and Referral together:
# - 5 acquired users
# - $210 total revenue
#
# Among active users:
# - Referral generates $120
# - Organic generates $60
#
# Comparing active users alone may exclude
# meaningful revenue from inactive customers.
# Always define the segment before reporting.
