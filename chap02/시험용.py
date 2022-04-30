
def reverse(x):
    q = 10 
    newx = 0
     

    while x > 0 :
      r = x % q
      x = x // q
      newx = newx*10 + r

    return newx

print(reverse(23))