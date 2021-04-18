friends = ["Banbon", "Karen", "Jim", "x", "y"]
friends[3] = "Mike"
friends.append(("Alex"))
friends.insert(1, "Gatw")

print(friends)

print("Alex index= " + str(friends.index("Alex")))
print("Alex count= " + str(friends.count("Alex")))

friends.sort()
print("Sorted= " + str(friends))

friends.reverse()
print("Reversed= " + str(friends))

friends2 = friends.copy()
print("Friends2= " + str(friends2))

numlist = list(range(5))
print("Numbers list= " +str(numlist))

friends.extend(numlist)
print("Friends + Numbers= " + str(friends))