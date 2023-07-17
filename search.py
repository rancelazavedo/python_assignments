def search(val1,val2):
    found=False
    index=0
    for i in range(0,len(val2)):
        if(val1 == val2[i]):
            found = True
            index=i
    
    if found == True:
        print("Found value",end=" ")
        print(val1)
        print("at location",end=" ")
        print(index)
        print("for "+val2)
    else:
        print("not found")

 
search('o',"clover")
search('a',"pluck")
