list1 = [2, 4, 6, 2, 4, 7, 8]

i = 0
list2 = []
list3=[]
while(i < len(list1)):
    j = i
    count = 0
    while(j < len(list1)):
        if list1[i] == list1[j]:
            count = count+1 
        j = j+1
    i = i+1
    list2.append(count)
print(list2)

# MyList = [1,3,2,1,4,2,3]
# my_dict = (i,MyList.count(i),for i in MyList:)

# print (my_dict)    #or print(my_dict) in python-3.x


lst = [1,3,2,4,1,5,4,3,7,9]
list={}
for i in lst:
    list[i]=lst.count(i)
print(list)
