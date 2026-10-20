A. total_mrr = users["monthly_revenue"].sum()

print(total_mrr)
B. pro_mrr = users[users["plan"] == 'Pro']["monthly_revenue"].sum()

print(pro_mrr)
C. starter_mrr = users[users["plan"] == 'Starter']["monthly_revenue"].sum()

print(starter_mrr)
Business Interpretation

