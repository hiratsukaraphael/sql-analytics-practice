
engaged_organic = users[(users["channel"] == "Organic") & (users["sessions_7d"] >= 2)]

print(engaged_organic)

active_paid = users[(users["channel"] == "Paid") & (users["sessions_7d"] >= 3)]

print(active_paid)

inactive_organic = users[(users["channel"] == "Organic") & (users["sessions_7d"] == 0)]

print(inactive_organic)
