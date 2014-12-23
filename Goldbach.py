CS303
=====

projects 


def is_Prime(n):
 divisor = 2
 while (divisor <= n / 2):
  if (n % divisor == 0):
   return False
  else:
   divisor += 1
 return True

def main():

  #Prompt the user to enter lower limit and upper limit

  lower_limit = eval(input('Enter lower limit:'))
  upper_limit = eval(input('Enter upper limit:'))

  max_pairs = 0
  pairs = 0

  #Find the sum of prime number
  for n in range(lower_limit, upper_limit + 1):
   if (n % 2 == 0):
    print(n, end="")
    for a in range(2, int(n/2)+1):
     if is_Prime(a):
      b = n - a
      if is_Prime(b) and (b + a == n):
       if (a <= b):
        pairs +=1
        if (pairs > max_pairs):
         max_pairs = pairs
        print("","=",a,"+",b,end="")
    pairs = 0
    print("")
     
  print("The maximum number of pairs =", max_pairs)

main()
