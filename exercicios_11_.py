henrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


print(henrix)
print(henrix[1])
print(henrix[1][2])


for i in range (len (henrix)): 
    print (henrix[i][i])
    for j in range (len(henrix[i])):
        print(henrix[i][j])
