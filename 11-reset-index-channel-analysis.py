
# ============================================================
# 11 - SERIES, DATAFRAME AND RESET_INDEX
# SaaS Acquisition Channel Analysis
# ============================================================

import pandas as pd

# Dataset: one row per acquired user

df = pd.DataFrame({
    "user_id": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109
    ],
    "channel": [
        "Organic", "Paid", "Organic",
        "Referral", "Paid", "Organic",
        "Referral", "Paid", "Organic"
    ],
    "revenue": [
        0, 90, 30, 20, 0,
        40, 60, 150, 20
    ]
})

print("ORIGINAL DATA")
print(df)


# TASK A - TOTAL REVENUE BY CHANNEL
# Selecting one column produces a Series.

revenue_by_channel = (
    df.groupby("channel")["revenue"].sum()
)

print("\nREVENUE BY CHANNEL")
print(revenue_by_channel)
print("Type:", type(revenue_by_channel))


# TASK B - CONVERT SERIES TO DATAFRAME

revenue_table = revenue_by_channel.reset_index()

print("\nREVENUE DATAFRAME")
print(revenue_table)
print("Type:", type(revenue_table))


# TASK C - UNIQUE USERS BY CHANNEL

users_by_channel = (
    df.groupby("channel")["user_id"].nunique()
)

print("\nUNIQUE USERS")
print(users_by_channel)


# TASK D - REVENUE PER ACQUIRED USER
# Pandas aligns both Series by channel index.

revenue_per_user = (
    revenue_by_channel / users_by_channel
)

print("\nREVENUE PER USER")
print(revenue_per_user.round(2))


# TASK E - CONVERT TO DATAFRAME AND SORT

result = revenue_per_user.reset_index(
    name="revenue_per_user"
)

result = result.sort_values(
    "revenue_per_user",
    ascending=False
)

print("\nFINAL RANKING")
print(result.round(2))


# CHECK EXPECTED RESULTS

assert revenue_by_channel["Paid"] == 240
assert revenue_by_channel["Organic"] == 90
assert revenue_by_channel["Referral"] == 80

assert users_by_channel["Paid"] == 3
assert users_by_channel["Organic"] == 4
assert users_by_channel["Referral"] == 2

assert revenue_per_user["Paid"] == 80
assert revenue_per_user["Referral"] == 40
assert revenue_per_user["Organic"] == 22.5

print("\nAll checks passed.")


# BUSINESS INTERPRETATION
#
# Paid:
#   Total revenue = $240
#   Unique users = 3
#   Revenue per acquired user = $80
#
# Referral:
#   Total revenue = $80
#   Unique users = 2
#   Revenue per acquired user = $40
#
# Organic:
#   Total revenue = $90
#   Unique users = 4
#   Revenue per acquired user = $22.50
#
# Paid has the highest revenue per user.
# However, this is not the same as profit.
# We need acquisition costs and retention
# before recommending increased spending.
