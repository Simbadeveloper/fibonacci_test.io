# fibonacci_test.io
what am learning about fibonacci.....<br >

#
Each new number in the Fibonacci sequence is generated by adding the previous two Fibonacci numbers. For example by starting with the numbers 1 and 2 being the first and second numbers in the Fibonacci sequence,<br > the first 10 numbers in the Fibonacci sequence looks like this:<br >
1, 2, 3, 5, 8, 13, 21, 34, 55, 89 <br >

<hr>
general formular:<br >

fibonacci(n) = Fibonacci(n-1) + fibonacci(n-2)<br >
<hr>

# Recursive
for a recursive function to stop calling itself we require some type of stopping condition.<br >
the recursion stop when it reach the base (end), every recurse function must have a base condition that stops the recursion or else the function calls itself inifinity.We must avoid infite recursion.<br >
If it is not the base case then we simplify our computation using the general formula<br >

stopping condition<br >
fibonacci(0) = 1<br >
fibonacci(1) = 1<br >

# Rules for writing recursive functions
1. know when to stop (the base)<br >
2. Decide how to take one step towards the base case<br >
3. Phrase the function in terms of one step and a smaller version of the original problem<br >

for numbers,  the base is usually a small interger  constant and a smaller version of the problem is something like n-1.<br >

# Recursive and factoral
To understand fibonacci you have to know about recursive and factoral.<br >
Recursive is a function which either calls itself or is in  a potential cycle of function calls.
 <hr>
Factorial of a  number is the product of all the interger from  to that number.<br >
for example the factorial of 6 (denoted 6!) is 1*2*3*4*5*6 = 720<br >
<hr>
formula
n! = n* (n-1)! <br >

0! = 1<br >
consider the examples<br >
1! =  1 * 0! = 1 * 1 = 1<br >
2! = 2 * 1!= 2 * 1 = 2<br >
3! = 3 * 2! = 3 * 2 = 6<br >

<hr >
def F(n):<br >
    if n == 0:<br > return 0<br >
    elif n == 1:<br > return 1<br >
    else:<br > return F(n-1)+F(n-2)<br >
 
#
    
    def F():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b 


# links to fibonacci resources
https://www.youtube.com/watch?v=lXyCRP871VI<br >

https://www.youtube.com/watch?v=4VrcO6JaMrM<br >

http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html<br >

https://en.wikipedia.org/wiki/Fibonacci_number<br >

https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence<br >


# checkout
look up for following......
1. The golden rule<br >
The golden ratio is the limit of the ratios of successive terms of the Fibonacci sequence (or any Fibonacci-like sequence), as originally shown by Kepler: <br >
Therefore, if a Fibonacci number is divided by its immediate predecessor in the sequence, the quotient approximates φ; e.g., 987/610 ≈ 1.6180327868852.<br >
<hr>

2. Memoization technique<br >
memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again
