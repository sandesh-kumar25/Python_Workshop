"""list slicing"""
list=[11,22,33,2,4,55,88,11]
print(list)
"""print(list[3:])
print(list[0:3])
print(list[0:])
print(list[-3:-7]) #wrong sequence/format of writing
print(list[-7:-3]) #Right format..
print(list[:-2])"""

""""x=list.clear()
print(x)"""

"""x=list.count(11)
print(x)"""
#output> 2   [kitne baar aaya hai list me ye dekhta hai]

x=list.append(47)  #to add something at last
print(list) 

x=list.pop()
print(x)  #by deafult it shows last element of list

list2=[2,4,6,8,10,"abc",'xyz']
list.extend(list2)
print(list)
