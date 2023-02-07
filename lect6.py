# Dictonary is nothing but key value pairs
# d1 = {}
# print(type(d1))
d2 = {"Raushan":"Lpu","Sonu":"CU","rahul":"Thapar","rockey":{"Rohan":"DPS","Rakesh":"DAV","Raju":"PSD"}}
#print(d2["rockey"]["Rohan"])#DPS
# d2["Ankit"]="RPS"
# d2[420]="GS"
# del d2[420]
# d3 = d2.copy()
# del d3["Raushan"]

# print(d2.get("Raushan"))
d2.update({"Ravi":"IITB"})
print(d2.values())
