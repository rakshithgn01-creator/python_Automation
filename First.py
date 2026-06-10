# print('Hello  Rakshith---Try to become great trader')

# # python.exe -m pip install --upgrade pip
# # this line can be 
# # comman d lin e
# a=int(input('Enter the number1:'))
# b=int(input('Enter the number2:'))
# c=int(input('Enter the number3:'))
# print('the value of number1',a)
# print('the value of number2',b)
# print('the value of number3',c)
# print('multiplication of a and b is:',a+b)
# print('multiplication of a and b is:',a-b)
# print('multiplication of a and b is:',a/b)
# print('multiplication of a and b is:',a*b)
# print('multiplication of a and b is:',a%b)
# a=2
# b=3
# print(a*b)
# print(a**b)

# a= 'Rakshith is a Good Boy '
# c='malayalam'
# print(a[0:1])
# print(a[0:])
# print(a[:7])
# print(a[:])
# print(a[0:7:2])
# b=(a[::-1])

# if a==b:
#     print('palindome')
# else:
#     print('Not a palindrome')
a= 'Rakshith is a Good Boy '
# c=a.lower()
# print(c)
# print(a)
# a.upper()
# a.capitalize()
# a.title()
# d=a.startswith('R')
# print(d)
# a.endswith('R')
# len(a)
# l=a.find("a")
# print(l)

# f=a.count('o')
# n=a.replace('Boy','trader')
# print(l)
# print(f)
# print(n)

# a='Rakshith is\n Good\t\"Boy\"\nbut also a great \'Trader\''
# print(a)

# b=input('Enter Your Name:')
# print('Good Afternoon,',b)
# print(f'Good Afternoon,{b}')

# a= '''Welcome aboard,<Name>
# Conragulation  and dateof joining is'<date>'''
# c=a.replace('<Name>','Rakshith').replace('<date>','12-may')
# print(c)

# a='Rakshith is a  good boy'
# # c=a.find(' ').replace('  ','ha')

# print(a.replace('  ','ha'))

l=[1,23,28,94,54,76,89,234]
# v=sum(l)
# # print(v)
# l.sort()
# print(l)
# l.reverse()
# print(l)
# print(l.pop(3))
# a=l.remove(54)
# print(a)
# l.append(456)
# l.extend([23,45,56])
# print(l)
# l2=l.copy()
# l.clear()
# print(l2)
# #Tuple
# t = (10, 20, 10, 30, 10)
# # # a=t.count(10)
# a=t.index(10)
# print(a)
# a=t*3
# # a=t+t
# a=min(t)
# b=max(t)
# c=sum(t)
# print(a)
# print(b)
# print(c)

# l=[]
# a=input('Enter the 1st fruit:')
# l.append(a)
# b=input('Enter the 2nd fruit:')
# l.append(b)
# c=input('Enter the 3rd fruit:')
# l.append(c)
# d=input('Enter the 4th fruit:')
# l.append(d)
# e=input('Enter the 5th fruit:')
# l.append(e)
# f=input('Enter the 6th fruit:')
# l.append(f)
# g=input('Enter the 7th fruit:')
# l.append()
# print(l)



# Dictionary

# a={'rakshi':100,'keshav':200,"shiva":4000}
# # # print(a['rakshi'])
# # # print(a.items())
# # print(a.keys())
# # print(a.values())
# # a['rakshi']=10000
# # print(a)
# print(a.update({'rakshi':500000,'agni':250000}))
# # print(a)
# print(a.get('rakshith'))
# d = {"a": 10, "b": 20,'c':30}

# x = d.pop("c")#remove that index key and value
# # y=d.popitem()#remove that last value

# # print(x)
# # print(y)
# # print(d)

# d = {"a": 1, "b": 2}

# # d.clear()
# c=d.copy()

# print(c)

# a={'rakshi':100,'keshav':200,"shiva":4000}
# b=a.get('rakshi1')
# c=a['rakshi']
# print(b)
# print(c)


# sets
# d={}
# print(type(s))

# s=set()
# print(type(s))

# s={1,2,3,4,6,6,7,7,8,9,76}
# print(s)


# a=s.add(234)
# s1=s.copy()
# s1=s.pop()
# s.add(345)# Single eleement
# s.update([20,30])#Multiple eleemert
# s.remove(768) # it will throw error if not found
# s.discard(76)#it will not throw error if not found
# s={1,2,3,4,5,6,6,7,7,8,9,76}
# t={2,3,4,5,98}
# print(s.union(t))
# print(s.intersection(t))
# print(s.issubset(t))#values of s present in t
# print(t.issubset(s))
# print(s.issuperset(t))#values of t present in s
# print(t.issuperset(s))
# print(s.symmetric_difference(t))
# print(s.difference(t))
# e={45,67}
# print(t.isdisjoint(e))
# print(s)

# s={}
# s['rakshi']=999
# s['keshav']=888
# print(s)

# s=set()
# i=input('enrter 1st number:')
# s.add(i)
# i=input('enrter 2st number:')
# s.add(i)
# i=input('enrter 3st number:')
# s.add(i)
# i=input('enrter 4st number:')
# s.add(i)
# i=input('enrter 5st number:')
# s.add(i)
# i=input('enrter 6st number:')
# s.add(i)

# i=input('enrter 7st number:')
# s.add(i)
# print(s)

# age=int(input('enter you age:'))
# if age >0:
#     if age>=18:
#         print('you are ready for voting')
#     else:
#         print('Not ready for voting')
# elif age<0:
#     print('age not measured in negative')
# else:
#     print('age shoudnot be 0')


# fruits = ["apple", "banana", "mango"]jupyter notebook

# fruits={'rakshi':100,'keshav':200,"shiva":4000}
# print(fruits['rakshi'])
# i=0
# while i in len(fruits):
#     print(i)
#     print(fruits[i])
#     i+=1

# print('exit from while loop')
# fruits={'rakshi':100,'keshav':200,"shiva":4000}
# keys=list(fruits.keys())
# i=0
# for fruit in fruits:
#     print(fruit)
#     print(fruits[fruit])

# fruits = ["apple", "banana", "mango"]
# for i in range(len(fruits)):
#     print(fruits[i])

# d = {'a':100, 'b':200}
# for x in d:
#     print(f" key is{x} and value is {d[x]}")

# for i in range(10, 0,-1):
#     print(i)

# for x,y in d.items():
#     print(x,y)


#While loop
# fruits={'rakshi':100,'keshav':200,"shiva":4000}
# keys=list(fruits.keys())

# while i<len(keys):
#     print(fruits[keys[i]])
#     i+=1

# break and continue

# for i in range(1,10,2):
#     if i==5:
#         break
#     print(i)

# for i in range(1,13,3):    
#     if i==7:
#         continue
#         print(i)
#     print(i)

# for i in range(1,13,3):
#     pass
# f={'rakshi':100,'keshav':200,"shiva":4000}
# for i in f.keys():
#     for j in f.values():
#         print(i,j)
# s=0
# for i in range(1,20):
#     s+=i
# print(s)

# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i}*{j}={i*j}')
    
# n=int(input('enter the factorial number:'))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# l=['rakshith','keshav','shiva','shubha']

# for i in l:
#     if i[0]=='s':
#         print(f'welocome aboard,{i}')

# n=5
# i=1
# while i<=10:
#     print(f'{n}*{i}={n*i}')
#     i+=1

# n=int(input('enter the number:'))
# for i in range(2,n):
#     if n%i==0:
#         print('number is not prime number')
#         break
# else:
#         print('number is prime')

# for i  in range(2,2):
#     print(i)


# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     print(' '*(n-i),end="")
#     print('*'*(2*i-1))
#     print(' ')

# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     # print(end='')
#     print('*'*(2*i-1))
#     # print(' ')

# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     if (i==1 or i==n):
#         print('*'*n)
#         print(end='')
#     else:
#        print('*',end="")   
#        print(" "*(n-2),end="")
#        print('*')
#     # print(' ')

# n=int(input('Enter the number:'))
# for i in range(10,0,-1):
#     # print(i)
#     print(f'{n}*{i}={n*i}')

# def som(**x):
#     print(x)

# som(a=5,b=6,c=12)

# def star(n):
#     if n==0:
#         return 0
#     print('*'*n)
#     print(star(n-1))

# star(3)


# f=open('first.txt')
# data=f.read()
# print(data)
# f.close()



# w='now i wot start trading'
# f=open('file.txt','w')
# f.write(w)
# n=open('file.txt')
# a=n.readlines()
# # c=n.readline()
# # d=n.readline()
# # print(a)
# print(c)
# print(d)
# n.close()

# f=open('file.txt')
# a=f.readline()
# while a!='':
#     print(a)
#     a=f.readline()

# f.close()   
# 

# with open('file.txt','r') as f:
#     print(f.read())

# with open('file.txt','a') as f:
#     print(f.write('am going to office'))

# with open('file.txt','w') as f:
#     f.write('keshav is my best frien')


# with open('file1.txt',"w") as f :
    # f.write('rakshith always ready to take but after his mental pressure he is not in a position to take risk now he is in survialval mode so avaoided everything,that distracts from his goal now and he will be back soon')

# with open('file1.txt','r') as f:

    # a=f.read()
    # print(a)
    # if 'mental' in a:
    #     print('the mental is present')
    # else:
    #     print('Not present')

  

# marks=[10,12,13,14,15,10,12,13,17,18,19]

# dict={}
# for i in marks:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1

# print(dict)
# dict1={}
# for i in dict:
#     if dict[i]==1:
#         dict1[i]=1

# print(dict1)

# a='banglore'
# print(a[3::-1])
# print(a[0:])
# print(a[-1::-1])
# print(a[::-1])
# print(a[::1])

# a='Rakshith Agni'
# s=a.split(' ')
# print(s)
# n=[]
# for i in s:
# #  print(s[i])
#  n.append(i[::-1])

# print(n)
# print(f"{n[0]} {n[1]}")
# # print("m")

# # a='rakshith'
# # l=''
# # for i in a:
# #     print(a)

a='akshay ranjal'
# '1ksh2y r3nj4l

s=''
l=1

for i in range(len(a)):
    print('i')
    if a[i]=='a':
        s=s+str(l)
        l=l+1
    else:
        s=s+a[i]

print(s)

