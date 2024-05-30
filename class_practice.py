'''class sam:
    def __init__(self,x):
        self.x=x
    def sqaure(self,x):
        print("Sqaure of number :",x*x)
    def cube(self,x):
        print("cube of the number :",x*x*x)    
s1=sam(5) # object 1
s2=sam(25) # object 2 
s1.sqaure(5)  # call on object
s2.sqaure(25) # call on object 2
s1.cube(5)
s2.cube(25)

class model:
    def model1(self,x1,x2):
        self.x1=x1
        self.x2=x2
    def Print_mode2(self,x1,x2):
        print(x1)
        print(x2)

object=model() # object instaized
object.model1("hondo","suzki") 
object.Print_mode2("hondo","suzki")

        
class calculate:
    def add(self,n1,n2):
        print(n1+n2)
    def mul(self,n1,n2):
        print(n1*n2)
    def div(self,n1,n2):
        print(n1/n2)

obj1=calculate() # object 
obj1.add(12,15)
obj1.mul(45,53)
obj1.div(10,2)


class squ:
    def square(self,n):
        print("suqare of given number is:",n*n)
object=squ()
object.square(6)

class cub:
    def cube(self,n3):
        print("cube of given number is:",n3*n3*n3)

cube1=cub()
cube1.cube(3)
cube1.cube(4) 
#-------------------------------------------------------------------------------------------
#Steps for checking Armstrong number: 

#Calculate sum of each digit's cube of a number.
#Compare that number with the resultant sum.
#If Number and Sum of digit's cube is equal then it is an Armstrong Number otherwise not.

# Define a class for Checking Armstrong number

class Check :
    # Constructor
    def __init__(self,number) :
        self.num = number       # 153 
    # define a method for checking number is Armstrong or not 
    def isArmstrong(self) :
        # copy num attribute to the temp variable
        temp = self.num  # temp=153
        res = 0          # res=0 
        # run the loop untill temp is not equal to zero
        while(temp != 0) :
            
            rem = temp % 10   #157 % 10 ==7

            res += rem ** 3  # 7 ** 3= 343= 3+4+3=10

            # integer division
            temp //= 10   # 157 // 10= 15

        # check result equal to the num attribute or not
        if self.num == res : # 157 ===157
            print(self.num,"is Armstrong")
        else :
            print(self.num,"is not Armstrong")


object=Check(127)   # object 
object.isArmstrong() # object call
s1=Check(153)  # object 2
s1.isArmstrong() #object2 call 


class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words('hello .py'))
'''
def rev(s1):
    print(s1[::-1])

rev('1111')    