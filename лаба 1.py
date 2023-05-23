a = float(input("Enter coefficient 'a' different from 0: "))
b = float(input("Enter coefficient 'b': "))
c = float(input("Enter coefficient 'c': "))
d = b**2-4*a*c  #discriminant
k1 = -b/(2*a)  #root at discriminant = 0
k2 = -b*0.5+d**0.5*0.5  #The first coefficient with discriminant > 0
k3 = -b*0.5-d**0.5*0.5  #The second coefficient with discriminant > 0
k4 = (-c)**0.5
if b == 0 and c > 0:
    print("no roots")
elif b == 0 and c < 0:
    print(k4)
elif d < 0:
    print("no roots")
elif d == 0:
    print(k1)
else:
    print(k2, k3)
