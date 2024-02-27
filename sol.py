import math
a=float(input("Старший коэффициент "))
b=float(input("Коэффициент при x "))
c=float(input("Свободный коэффициент "))
D=b**2-4*a*c
if D>0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=((-b)-math.sqrt(D))/(2*a)
    if x1==int(x1): x1=int(x1)
    if x2==int(x2): x2=int(x2)
    print(x1)
    print(x2)
elif D==0:
    x=-b/(2*a)
    if x==int(x): x=int(x)
    print(x)
else:
    print("нет корней")
j=100
print(type(j)==int)
a=input("нажмите любую кнопку для выхода")
