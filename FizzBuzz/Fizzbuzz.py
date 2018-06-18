#fizzbuzz checking number divisible by both 5,3
#and both 5 and 3 in range 100

for x in range(1,101):

 if x % 3==0 and x %5==0:
   print("FizzBuzz")
elif x%3==0:
   print("Fizz")
elif x%5==0:
   print("Buzz")
else:
  print(x)

