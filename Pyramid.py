def pyramid(n):
    val1='*'
    val2=" "
    n2=n
    for i in range(0,n):
        for j in range(0,n2):
            val2=val2+" "
        n2=n2-1
        print(val2+val1)
        val1=val1+'**'
        val2=" "

pyramid(6)