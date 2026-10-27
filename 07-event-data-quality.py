
# ============================================================
# 07 - EVENT DATA QUALITY ANALYSIS
# ============================================================
# Skills:
# Pandas, value_counts(), drop_duplicates(),
# Boolean filtering, marketing channel analysis
#
# Business scenario:
# Identify duplicated SaaS tracking events and determine
# how they affect signup and purchase reporting.
# ============================================================

import pandas as pd

# 1. CREATE DATASET

events = pd.DataFrame({
    "event_id": [101, 102, 103, 103, 104, 105, 105, 106],
    "channel": [
        "Organic", "Paid", "Paid", "Paid",
        "Organic", "Paid", "Paid", "Organic"
    ],
    "event_type": [
        "signup", "signup", "purchase", "purchase",
        "purchase", "signup", "signup", "signup"
    ]
})

print("ORIGINAL DATASET")
print(events)


# 2. TASK A - COUNT EVENTS BEFORE CLEANING

signup_before = events["event_type"].value_counts()["signup"]
purchase_before = events["event_type"].value_counts()["purchase"]

print("\nEVENTS BEFORE CLEANING")
print("Signups:", signup_before)
print("Purchases:", purchase_before)


# 3. TASK B - REMOVE DUPLICATE EVENTS

clean_events = events.drop_duplicates(subset=["event_id"])

print("\nCLEANED DATASET")
print(clean_events)


# 4. TASK C - COUNT EVENTS AFTER CLEANING

signup_after = clean_events["event_type"].value_counts()["signup"]
purchase_after = clean_events["event_type"].value_counts()["purchase"]

print("\nEVENTS AFTER CLEANING")
print("Signups:", signup_after)
print("Purchases:", purchase_after)


# 5. TASK D - PURCHASES BY MARKETING CHANNEL

purchases = clean_events[
    clean_events["event_type"] == "purchase"
]

purchases_by_channel = purchases["channel"].value_counts()

print("\nPURCHASES BY CHANNEL")
print(purchases_by_channel)


# 6. BUSINESS INTERPRETATION

print("\nBUSINESS INTERPRETATION")
print("Signups removed:", signup_before - signup_after)
print("Purchases removed:", purchase_before - purchase_after)

# Findings:
# - Original dataset: 8 events
# - Cleaned dataset: 6 events
# - Signups decreased from 5 to 4
# - Purchases decreased from 3 to 2
# - Paid purchases: 1
# - Organic purchases: 1
#
# Conclusion:
# Duplicate tracking events inflated both signup and
# purchase counts. Cleaning event IDs improves the
# accuracy of marketing performance reporting.
#
# Important:
# This assumes event_id uniquely identifies a real event.
# In production, validate that assumption before deduplication.
