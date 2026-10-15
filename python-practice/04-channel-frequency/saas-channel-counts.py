
channel_counts = users["channel"].value_counts()

print(channel_counts)

active_channel_counts  = users[users["sessions_7d"]>=3]["channel"].value_counts()

print(active_channel_counts )

inactive_channel_counts = users[users["sessions_7d"]==0]["channel"].value_counts()

print(inactive_channel_counts)

#It is the same as 

active_users = users[users["sessions_7d"] > 0]
print(active_users)
channels = active_users["channel"]

print(channels)

channel_counts = channels.value_counts()
print(channel_counts)
