import numpy as np
import matplotlib.pyplot as plt
import time

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
  return(counter)

starttime = time.time()
#creating lists to add to for each x in range
l = [0]
l1 = [0]
for x in range (1,1000000):
    count = collatz(x)
    #storing C(n) in list l each time collatz runs
    l.append(count)
    #making y scale log10(n)
    logx=np.log10(x)
    #storing log10(n) in list l1 for each n
    l1.append(logx)

#finding the integer which had the maximum number of iterations
maxC=max(l)
integer=l.index(maxC)
print("Integer with max. iterations is",integer)

endtime = time.time()

elapsed = endtime-starttime

print("Completed in",elapsed,"s")

#plotting C(n) (stored in l) vs. log10(n) (stored in l1)
plt.plot(l1,l)
#labelling the axes and adding graph title
plt.title('C(n) versus log10(n)')
plt.ylabel('C(n)')
plt.xlabel('log10(n)')
plt.show()
