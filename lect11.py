# i = 0
# while(True):
#     if i+1<5:
#         i = i + 1
#         continue
#     print(i+1,end=" ")
#     if(i==44):
#         break
#     i=i+1
# +++++Quiz+++++++
while(True):
    inp = int(input("Enter a number\n"))
    if inp>100:
        print("Congrats you printed grater than 100\n")
        break
    else:
        print("Try again\n")
        continue
