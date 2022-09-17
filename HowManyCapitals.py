def capital_indexes(string):
    list1=[]
    list2=[]
    list1[:0]=string
    x = 0
    while len(list1) > 0:
        if list1[0].isupper() == True:
            list2.append(x)
            list1 = list1[1:]
            x = x + 1
        else:
            list1 = list1[1:]
            x = x + 1
    return list2

str1= "BEANSofChEse2"
print(capital_indexes(str1))