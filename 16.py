sowmi1,sa2=map(int,input().split())
for i in range(sowmi1+1,sa2,1):
  if(i>1):
    for j in range(2,i):
      if(i%j==0):
        break
     else:
      print(i,end='')
