def reverse(x):
    x = str(x)
    newx = ''

    for c in x:
        newx = c + newx

    print(newx)

    
    return int(newx)
  

print(reverse(3700))