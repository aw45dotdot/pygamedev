list = ["friend1","friend2","friend3","friend4","friend1","friend2","friend3","friend4"]

print(f'the list is {list}\n')
print(f'total items in list: {len(list)}\n') #total count
print(f'total time friend2 repeated: {list.count("friend2")}')  #specific item counter

#difference between append and extend
list.append("friend5")
print(f'the list is {list}\n')

list2 = ["maths","cspe","business","french"]

list.append(list2)
print(f'the list is {list}\n')

list3 = ["hello"]

list3.extend(list2)
print(f'the list is {list3}\n')
list.remove("friend5")
print(f'the list is {list}\n')
list.pop(0)
print(f'the list is {list}\n')
list2.index("business")
print(f'the list is {list}\n')
