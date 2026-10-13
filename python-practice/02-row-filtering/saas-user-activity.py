
active_users = users[users["sessions_7d"] >=  3]

print(active_users)

paid_users = users[users["channel"] == 'Paid']

print(paid_users)

inactive_users = users[users["sessions_7d"] == 0 ]

print(inactive_users)
