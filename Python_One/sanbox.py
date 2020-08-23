# mystring = 'abcdef'
# x = mystring.split()
# print(x)


#List
myList = [1,2,3,'stringabc',True,[3,2,1]]
listtwo = ['x','y','z']
#myList[0] = 'New item'
#myList.append("Another new item")
# myList.extend(listtwo)
item = myList.pop()

print(myList)
print(item)

#Tuples

#boolean

#set
converted = set([1,1,1,1,2,3,3,2,2,2,2,3,3,3])

print(converted)

#tuples unpacking
mypairs = [(1,2),(3,4),(5,6)]

for tup1,tup2 in mypairs:
    print(tup2)
    print(tup1)

#list comprehesion

x = [1,2,3,4]

out = []
for num in x:
    out.append(num)
print(out)

#Become
out = [num for num in x]

print(out)
