
# ============================================================
# 10 - ACQUISITION CHANNEL REVENUE RANKING
#
# Skills:
# groupby(), sum(), sort_values(), nunique()
# Revenue per user and business interpretation
# ============================================================

import pandas as pd

# 1. CREATE DATASET

df = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "channel": [
        "Organic", "Paid Search", "Referral",
        "Organic", "Paid Search", "Referral",
        "Organic", "Paid Search", "Referral",
        "Organic"
    ],
    "revenue": [
        0, 120, 80, 30, 0, 50, 70, 200, 0, 40
    ]
})

print("ORIGINAL DATA")
print(df)


# 2. TASK A - TOTAL REVENUE BY CHANNEL

revenue_by_channel = (
    df.groupby("channel")["revenue"].sum()
)

print("\nTOTAL REVENUE BY CHANNEL")
print(revenue_by_channel)


# 3. TASK B - RANK CHANNELS BY REVENUE

ranked_revenue = revenue_by_channel.sort_values(
    ascending=False
)

print("\nREVENUE RANKING")
print(ranked_revenue)


# 4. TASK C - COUNT UNIQUE USERS

users_by_channel = (
    df.groupby("channel")["user_id"].nunique()
)

print("\nUNIQUE USERS BY CHANNEL")
print(users_by_channel)


# 5. TASK D - REVENUE PER ACQUIRED USER

revenue_per_user = (
    revenue_by_channel / users_by_channel
)

ranked_rpu = revenue_per_user.sort_values(
    ascending=False
)

print("\nREVENUE PER ACQUIRED USER")
print(ranked_rpu.round(2))


# 6. TASK E - BUSINESS INTERPRETATION

print("\nBUSINESS FINDINGS")

print("Highest revenue channel:",
      ranked_revenue.index[0])

print("Highest total revenue:",
      ranked_revenue.iloc[0])

print("Highest revenue per user channel:",
      ranked_rpu.index[0])

print("Highest user count channel:",
      users_by_channel.idxmax())

# EXPECTED RESULTS:
#
# Total revenue:
# Paid Search = $320
# Organic = $140
# Referral = $130
#
# Unique users:
# Organic = 4
# Paid Search = 3
# Referral = 3
#
# Revenue per acquired user:
# Paid Search = $106.67
# Referral = $43.33
# Organic = $35.00
#
# BUSINESS INTERPRETATION:
#
# Organic acquired the most users.
# Paid Search generated the most revenue.
#
# The channel with the most users does not
# necessarily generate the most revenue.
#
# IMPORTANT:
# Revenue is not the same as profit.
# Marketing costs, retention and attribution
# should be considered before making
# investment decisions.
#
# This is a small illustrative dataset.
