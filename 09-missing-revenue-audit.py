
# ============================================================
# 09 - MISSING REVENUE AUDIT
#
# Skills:
# isna(), boolean filtering, value_counts(),
# groupby(), sum(), data quality
# ============================================================

import pandas as pd

# 1. CREATE DATASET

df = pd.DataFrame({
    "user_id": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110
    ],
    "plan": [
        "paid", "trial", "paid", "paid", "trial",
        "paid", "trial", "paid", "paid", "paid"
    ],
    "monthly_revenue": [
        49, None, 99, None, None,
        49, None, 99, None, 49
    ]
})

print("ORIGINAL DATA")
print(df)


# 2. TASK A - COUNT MISSING REVENUE VALUES

missing_count = df["monthly_revenue"].isna().sum()

print("\nMISSING REVENUE COUNT")
print(missing_count)


# 3. TASK B - DISPLAY ROWS WITH MISSING REVENUE

missing_rows = df[df["monthly_revenue"].isna()]

print("\nUSERS WITH MISSING REVENUE")
print(missing_rows)


# 4. TASK C - MISSING REVENUE BY PLAN

missing_by_plan = missing_rows["plan"].value_counts()

print("\nMISSING REVENUE BY PLAN")
print(missing_by_plan)


# 5. TASK D - RECORDED REVENUE BY PLAN

revenue_by_plan = (
    df.groupby("plan")["monthly_revenue"].sum()
)

print("\nRECORDED REVENUE BY PLAN")
print(revenue_by_plan)


# 6. ADDITIONAL QUALITY METRIC

missing_percentage = (
    missing_count / len(df)
) * 100

print("\nMISSING REVENUE PERCENTAGE")
print(f"{missing_percentage:.2f}%")


# 7. TASK E - BUSINESS INTERPRETATION

print("\nBUSINESS INTERPRETATION")

print("Total users:", len(df))
print("Missing revenue values:", missing_count)
print("Missing percentage:", missing_percentage)

print(
    "Paid users with missing revenue:",
    missing_by_plan["paid"]
)

# FINDINGS:
#
# - 10 users in the dataset
# - 5 missing revenue values (50%)
# - 3 trial users have missing revenue
# - 2 paid users have missing revenue
# - Recorded paid revenue: $345
#
# BUSINESS CAUTION:
#
# The $345 is the total of KNOWN paid revenue.
# It may understate actual paid revenue because
# two paid accounts have unknown amounts.
#
# Pandas sum() skips missing values by default.
# For the trial plan, it returns 0 even though
# all trial revenue values are missing.
#
# Missing revenue should not automatically
# be treated as zero without a valid
# business rule.
#
# NEXT ACTION:
# Verify the paid users' revenue records
# against the billing system before reporting
# final revenue metrics.
