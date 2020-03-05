import time

def addition():
  N1 = int(input("Number 1 : "))
  N2 = int(input("Number 2 : "))
  return N1+N2
def subtraction():
  N1 = int(input("Number 1 : "))
  N2 = int(input("Number 2 : "))
  return N1-N2
def division():
  N1 = int(input("Number 1 : "))
  N2 = int(input("Number 2 : "))
  return N1/N2
def Multiplication():
  N1 = int(input("Number 1 : "))
  N2 = int(input("Number 2 : "))
  return N1*N2
def main():
  print ("What Do You Want To Do")
  print ("1 Addition, 2 subtraction, 3 division, 4 Multiplication, 5 Exit")
  option = int(input("Choose "))
  while option != 5:
    if option == 1:
      print (addition())
      print ("What Do You Want To Do")
      print ("1 Addition, 2 subtraction, 3 division, 4 Multiplication, 5 Exit")
      option = int(input("Choose "))
    if option == 2:
      print (subtraction())
      print ("What Do You Want To Do")
      print ("1 Addition, 2 subtraction, 3 division, 4 Multiplication, 5 Exit")
      option = int(input("Choose "))
    if option == 3:
      print (division())
      print ("What Do You Want To Do")
      print ("1 Addition, 2 subtraction, 3 division, 4 Multiplication, 5 Exit")
      option = int(input("Choose "))
    if option == 4:
      print (Multiplication())
      print ("What Do You Want To Do")
      print ("1 Addition, 2 subtraction, 3 division, 4 Multiplication, 5 Exit")
      option = int(input("Choose "))

main() 