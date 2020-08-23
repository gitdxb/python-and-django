def my_func(param1='defaut value'):
    print('My first python function')

my_func()


#Sum

def addSum(num1,num2):
    if type(num1) == type(num2) == type(10):
      return num1 + num2
    else:
        return "Sorry I need intergers"

result = addSum(2,'3')
print(result)


#Checking even number from a list
mylist = [1,2,3,4,5,6,7,8,9]

def even_bool(num):
    return num%2 == 0
evens = filter(even_bool,mylist)
#filter() accept a func and sequence, it will print a list if the func return true
print(list(evens))
