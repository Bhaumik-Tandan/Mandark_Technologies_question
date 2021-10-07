def pri_str(string, prev, n, k):
    if (not k) :
        print(prev)
        return

    for i in range(n):
        newprev = prev + string[i]
        pri_str(string, newprev, n, k - 1)
 

# it is given in the question that we have to  
# print string of len 3 and input string is also of len 3
pri_str(sorted(list(input("Enter the string: "))),"", 3, 3)