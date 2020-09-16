def collatz(n):
  counter=0

  while n>1:
    if (n % 2)== 1:
      #n is odd
      n=3*n + 1
    else:
      #n is even
      n=n/2
    counter=counter+1
    #increases iteration counter by 1
    print(n)
  print("C(n)=",counter)
n = int(input('Enter n: '))
collatz(n)


