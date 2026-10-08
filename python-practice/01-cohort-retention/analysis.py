# Step 1: Convert dates
users["signup_date"] = pd.to_datetime(users["signup_date"])
events["activity_date"] = pd.to_datetime(events["activity_date"])

# Step 2: Create signup cohort (week starting Monday)
users["cohort_week"] = users["signup_date"] - pd.to_timedelta(users["signup_date"].dt.weekday,unit="D")

# Step 3: Join users and events
df = users.merge(events, on="user_id", how="left")

# Step 4: Calculate days since signup
df["days_since_signup"] = (df["activity_date"] - df["signup_date"]).dt.days

# Step 5: Filter Week 1 activity
week1 = df[(df["days_since_signup"] >= 7) & (df["days_since_signup"] <= 13)]

# Step 6: Count retained users by cohort
retained = week1.groupby("cohort_week")["user_id"].nunique()

# Step 7: Count total users by cohort
total = users.groupby("cohort_week")["user_id"].nunique()

# Step 8: Combine results and calculate retention
result = pd.concat([total, retained], axis=1)
result.columns = ["total_users", "retained_users"]
result["retained_users"] = result["retained_users"].fillna(0)
result["retention_rate"] = result["retained_users"]/result["total_users"]*100
result
