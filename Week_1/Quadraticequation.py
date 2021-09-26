import cmath
print("General Form:- ax**2 + bx + c = 0")

a=int(input("Enter a(a!=0): "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

d=(b**2)-(4*a*c)

sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)

print("\n")
print(f"Results for equation, {a}x**2+{b}x+c{c}+0, are:-\n ")

if d>0:
    print("Type of Roots: Two Distinct Real Roots")
elif d==0: 
    print("Type of Roots: Two Equal Real Roots")
elif d<0:
    print("Type of Roots: Two Complex Roots")

print(f"The solutions are {sol1} and {sol2}")
