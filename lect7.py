# it always accept unique values
s = set()
#print(type(s))
# l = [1,2,3,4]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))
s.add(1)
s.add(2)
s1 = s.union({1,2,3})
s1 = s.intersection({1,2,3})
print(s,s1)
