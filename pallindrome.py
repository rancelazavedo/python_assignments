def pallindrome(val1):
    val2=""
    n=len(val1)
    for i in range(0,n):
        val2 = val2 + val1[n-i-1]
    print(val2)
    if val1 == val2:
        print(val1 + " is a pallindrome")
    else:
        print(val1 + " is not a pallindrome")

val="banana"

pallindrome(val)