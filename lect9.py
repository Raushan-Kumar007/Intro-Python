# list1 = [["Ravi",1],["Raushan",2],["Rahul",5],["Razz",24]]
# for item in list1:
#     print(item)
# dict1 = dict(list1)

# for item in dict1:
#     print(item)
# for item,bread in dict1.items():
#     print(item,bread)
# +++++quize++++
list1 = [int,float,"Ravi",12,3,5,7,11,6]
for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)