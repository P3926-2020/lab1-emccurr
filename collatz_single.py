def collatz(n):
  counter=0

  while n>1:
    if (n % 2)== 1:
      n=3*n + 1
    else:
      n=n/2
    counter=counter+1
    print(n)
  print("C(n)=",counter)
n = int(input('Enter n: '))
collatz(n)

