#ID: 20CE045
#NAME: YASHVI KOTADIYA

T = int(input())                #number of test cases
for i in range(T):
    n = input()                 #take string from user
    l = len(n)                  #length of string
    if l % 2 == 0:              #check whether the length is divisible by 2 or not
        x = n[:l//2]            #slicing
        y = n[l//2:]            #slicing
    else:
        x = n[:l//2]            #slicing
        y = n[l//2+1:]          #slicing

    if sorted(x) == sorted(y):  #compare the two sorted string
        print("YES")
    else:
        print("NO")
