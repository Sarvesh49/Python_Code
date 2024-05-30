'''class Evenodd:
    def number(self,n):
        self.n=n # access n variable
        if n%2==0:
            print("number is even:",n)
        elif n<0:
         print("number is negative",n)
        else:
            print("number is odd:",n)

s1=Evenodd() 
s1.number(-1)
s1.number(5)
s1.number(4)'''
#-------------------------------------------------------------------------------
'''
class Leap_year:
   def year(self,y1):
      self.y1=y1
      if y1%4==0:
         print("enter year is leap year:",y1)
      elif y1%400==0:
         print("Entered century is leap yaer:",y1)
      else:
         print("entered number is not a leap year:",y1)
obj1=Leap_year()
obj1.year(2024)
obj1.year(2001)
obj1.year(1000)
'''
#ch=input("Please Enter Your Own Character : ")

class alpha:
   def values(self,ch):
    self.ch=ch
    if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
       print("The Given Character ", ch, "is an Alphabet")
    else:
      print("The Given Character ", ch, "is Not an Alphabet")
         
c1=alpha()
c1.values("a")
c1.values("*")