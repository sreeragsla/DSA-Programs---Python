from array import *
exp=array('i',(0,1,2,3,4,8))
print(exp)

#We are accessing by using the for loop

for i in exp:
    print(i)

#In this below program iam accessing particular element and iam replacing with new value
    
for i in range(len(exp)):
    if exp[i]==8:
        exp[i]=10
    print(exp[i])

#After replacing the new element printing the array

    
print(exp)


