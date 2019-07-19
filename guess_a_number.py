import random
import math

def verify(in1,in2):
    if in1>in2:
        out = 1
    elif in1<in2:
        out = -1
    else:
        out = 0
    return out
    
max = 1000000
nb = random.randint(1,max)
# nb = 889801
print('nb = ', nb)
guess = 1;

out = max/2
temp = out
while guess < 50:
    v = verify(out,nb)
    
    if temp < 2:
        temp = temp * 2
    else:
        temp = temp / 2
        
    if v == 1:
        out = out - temp
    elif v == -1:
        out = out + temp
    else:
        print 'out = ',out,'and nb = ',nb,' and guesses taken = ',guess
        break
    guess = guess + 1
#     print 'temp = ' ,temp
#     print 'out = ' ,out
