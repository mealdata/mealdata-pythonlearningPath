countries =[ "Kenya", "Ethiopia", "Uganda", "Nigeria", "Mali", "South Sudan"]
countries2 =list(("SouthAfrica ", "Amerca", "Jerman", "Awropa", "Talian", "Djiabout"))
print(countries)

# indexing the string 
print(countries[0])
print(countries[:2])
print(countries[2:])
print(countries[0:4])
countries[0] = "South Africa" # here the Kenya will replaced by South Africa
print(countries)
print(type(countries2))
print(type(countries))

countries.extend(countries2)

print(countries)

countries.remove('Mali')

countries.append("USA")

print(countries)

# to clear all list use, countries.clear()
