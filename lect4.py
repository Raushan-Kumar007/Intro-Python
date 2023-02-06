mystr = "Ravi is a good boy"
print(len(mystr))
print(mystr[0])#R
print(mystr[0:4])#Ravi
print(mystr[0:18])#Ravi is a good boy
#print(mystr[78])#Error
print(mystr[0:78])#Ravi is a good boy
print(mystr[:4])#Ravi
print(mystr[:])#Ravi is a good boy
print(mystr[0:4:2])#Rv
print(mystr[::])#Ravi is a good boy
print(mystr[-4:-2])# b
# when negative number comes count it from right like -1,-2...
print(mystr[::-1])#yob doog a si ivaR
print(mystr[::-2])#ybdo  iia
# it'll first reverse the string and then skips 2 letters
