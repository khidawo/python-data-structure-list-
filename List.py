#creating a list

cars=["mercedes","Ford","Dodge challenger"]
print(cars)
#list can be of any data types
cars1=["21","mercedes","true","cherry"]
print(cars1)

#list inside a list
student=["4","76","34","23"],["John","Peter","Caleb"],[True,False]
print(cars1[1:2])

#checking if an item exist in a list
students=["love","ken","lucid","quavo"]
if "John"in students:
    print("Yes,lucid in the list")
else:
    print("No such name in student")


 #changing items in the list
group=["love","ken","lucid","quavo"]
group[2]="takeoff"
print(group)
#adding items to a list
group.append("killian")
#append add items at the end of the list
#insert add items at specified index
group.insert(2,"Nimoh")
group.pop(2)
print(group)

#loop through a list
for x in group:
    print(x)
#looping through a list using index number    
for i in range(len(group)):
    print(group[2])


 
