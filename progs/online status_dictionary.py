def online_count(statuses):
    count=0
    for i in (statuses):
        print(statuses[i])
        if statuses[i]=="online":
            count+=1
    return count
    
    
statuses={
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
x=online_count(statuses)
print("the number of people online are", x)