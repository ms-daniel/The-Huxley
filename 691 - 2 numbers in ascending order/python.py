aux = input().split()
aux.sort()
print(aux[0] + ' ' + aux[1]) 

"""
or 

aux = input().split()
n1 = int(aux[0])
n2 = int(aux[1])

if n2 < n1:
    aux = n2
    n2 = n1 
    n1 = aux

print(n1, n2) 

"""