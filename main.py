myname=input("Enter your name: ")
print("Hi", myname)
marks=int(input("Enter your marks: "))

if marks>=90 and marks<=100:
  print("Hi", myname, " you scored Grade A* ")
elif marks>=80 and marks<=89:
  print("Hi", myname, "you scored Grade A ")
elif marks>=70 and marks<=79:
  print("Hi", myname, "you scored Grade B ")
elif marks>=60 and marks<=69:
  print("Hi", myname, "you scored Grade C ")
else:
  print("Hi", myname,"Have another go!")
  
