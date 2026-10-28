
# ============================================================
# 08 - USER CONVERSION FUNNEL ANALYSIS
# Path: python-practice/08-user-funnel-nunique.py
#
# Skills:
# Pandas, value_counts(), groupby(), nunique(),
# conversion rates, product funnel analysis
# ============================================================

import pandas as pd

# 1. CREATE DATASET

events = pd.DataFrame({
    "user_id": [
        1, 1, 1,
        2, 2,
        3, 3,
        4, 4, 4,
        5,
        6, 6, 6
    ],
    "event_type": [
        "signup", "activate", "purchase",
        "signup", "activate",
        "signup", "activate",
        "signup", "activate", "purchase",
        "signup",
        "signup", "activate", "activate"
    ]
})

print("ORIGINAL EVENTS")
print(events)


# 2. TASK A - COUNT EVENT ROWS

event_counts = events["event_type"].value_counts()

print("\nEVENT COUNTS")
print(event_counts)


# 3. TASK B - COUNT UNIQUE USERS PER EVENT TYPE

unique_users = (
    events.groupby("event_type")["user_id"].nunique()
)

print("\nUNIQUE USERS PER STAGE")
print(unique_users)


# 4. TASK C - CALCULATE FUNNEL CONVERSION RATES

signups = unique_users["signup"]
activations = unique_users["activate"]
purchases = unique_users["purchase"]

signup_to_activation = activations / signups * 100
signup_to_purchase = purchases / signups * 100
activation_to_purchase = purchases / activations * 100

print("\nFUNNEL CONVERSION RATES")

print(
    f"Signup to Activation: "
    f"{signup_to_activation:.2f}%"
)

print(
    f"Signup to Purchase: "
    f"{signup_to_purchase:.2f}%"
)

print(
    f"Activation to Purchase: "
    f"{activation_to_purchase:.2f}%"
)


# 5. TASK D - BUSINESS INTERPRETATION

print("\nBUSINESS INTERPRETATION")

print(
    "Activation events:",
    event_counts["activate"]
)

print(
    "Unique activated users:",
    activations
)

print(
    "Repeated activation events:",
    event_counts["activate"] - activations
)

# Findings:
# - 6 users signed up
# - 5 unique users activated
# - 2 unique users purchased
# - Signup-to-activation conversion: 83.33%
# - Signup-to-purchase conversion: 33.33%
# - Activation-to-purchase conversion: 40.00%
#
# There are 6 activation events but only 5
# unique activated users because user 6
# activated twice.
#
# Repeated events are not necessarily bad data.
# Counting distinct users prevents overstating
# how many people reached each funnel stage.
#
# Production note:
# Validate event timestamps, stage ordering,
# and cohort definitions for a true funnel.
