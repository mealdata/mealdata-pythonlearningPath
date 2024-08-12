# only two loop nested, 
my_list = [

[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15]
]

# print(my_list[0][0]) # The output will be 1
# print(my_list[1]) # the output is [6,7,8,9,10]

for lists in my_list:
    for column in lists:
         print(column)

# Three loop nested
mydata = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
for lists in mydata:
    for sublist in lists:
        for element in sublist:
            print(element)
