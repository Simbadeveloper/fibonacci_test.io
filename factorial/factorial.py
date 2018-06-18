#factorial test
def factorial(n):
    ni = int(n)
    
  if ni !=n or ni<=0:
    raise ValueError("%s is not a positive interger." %n)
    
 if ni == 1:
    return 1

return ni * factrorial(ni -1)
