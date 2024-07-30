#local versus global 
def local():
    m=7
    print(m)
m=12  # here this m=12 is global scopes
print(m)
local() # we write local() function to print out the local m=7