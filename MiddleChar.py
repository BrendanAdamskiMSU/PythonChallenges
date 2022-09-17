def mid(string):
    List = []
    List[:0] = string
    midChar = ((len(List)/2)-.5) 
    midChar = int(midChar)
    wordNumber = (len(List) % 2)
    none = ""
    if wordNumber == 1:
        return List[midChar]
    else:
        return none
    
    
x = "abchgyuhj"
print(mid(x))