'''city=["nagpur","bhandara","madua","ramtek","amrivta","gondia"]
dist=["nagpur","bhandara","madua","ramtek"]

def print_unique_city(city,dist):
  unique_city=[city for city in city if all(city not in dist for dist in dist)]
  print(unique_city)

print_unique_city(city,dist)  

list1=[1,2,3,4,56,7]
list2=[4,5,67,89,90]
list1.sort()
print(list1)
list2.sort()
print(list2)
for i in list1:
    print(i)
    for j in list2:
        print(j)
if len(list1)!=len(list2):
    print(list1+list2)


class Even:
    def evenodd(n1):
      if n1%2==0:
        print("Number is even",n1)
      else:
        print("Number is odd",n1)    
    
    evenodd(10024)   
   
def model(m1,m2,m3):
   for m1 in range(m1):
      if m1%2==0:
         print(m1)
      for m2 in range(m2):
       if m1%2!=0:   
         print(m2)
         for m3 in range(m3):
            print(m3)

model(5,10,15)

numbers=[2,3,2,3,4,5,6]
min =numbers[0]  
max=numbers[0]  
for i in range(len(numbers)):
      if numbers[i]>max:
        max=numbers[i]
      elif numbers[i] < min:
        min =numbers[i]
print("MIN",min)
print("MAX",max)

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
'''
'''
password=int(input())
user_password=int(input())
if password!=user_password:
  raise Exception("inavlid password!")
elif password==user_password:
  print("valid password!")
'''
import re
count=0
match=re.finditer("i","HiaHiHiaHi")
for i in match: # loop 4 times exeute
  count+=1
  print(i.start()," ",i.end()," ",i.group())
print("The number of occurrence :",count)  

