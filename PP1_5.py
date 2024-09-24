
def q1():
  #Write Assignment code here
  Num= input("Input a integer: ")
  Num= int(Num)
  print(f"Your integer + 3 is: {Num + 3} ")
 

def q2():
  #Write Assignment code here
  num1= input("Input a number: ")
  num1= float(num1) + 4
  print(f"Your number + 2 is: {num1 + 2} ")

def q3():
  #Write Assignment code here
  num2= input("Input a radius: ")
  radius = float(num2)
  Pi= 3.14
  area= Pi*(radius**2)
  print(f"The area of a circle is: ",area)
def q4():
  #Write Assignment code here
  word= input("Input a number: ")
  word= float(word) 
  twelve= 12
  word2= twelve*word
  word2= int(word2)
  print(f"Your whole number * 12 is: ",word2)

def q5():
  #Write Assignment code here
  num3= input("Input a integer: ")
  num3= int(num3) + 5
  print(f"Your number + 5 is {num3}"  )

#Comment this code out when running tests
#Do not comment this out when running your program normally

q1()
q2()
q3()
q4()
q5()
