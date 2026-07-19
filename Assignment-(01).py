def check():
    global a,b,c
    a = int(input("Enter first side of the triangle: "))
    b = int(input("Enter second side of the triangle: "))
    c = int(input("Enter third side of the triangle: "))
    if a > 0 and b > 0 and c > 0: 
        if (a + b >= c) and (b + c >= a) and (c + a >= b):
            return True
    else:
        print("The triangle is not valid.")

def perimeter():
    global peri
    peri = a+b+c
    print("The perimeter of the triangle is: ",peri)

def type():
    if a == b == c:
        print("The triangle is an equilateral triangle.")
    elif a == b or b == c or c == a:
        print("The triangle is an isosceles triangle.")
    elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        print("The triangle is a right-angled triangle.")    
    elif a != b and b != c and c != a:
        print("The triangle is a scalene triangle.")

def area():
    if a == b == c:
         area = (a**2 * 3**0.5) / 4
    elif a == b or b == c or c == a:
        if a == b:
            height = (a**2 - (c/2)**2)**0.5
            area = (c * height) / 2
        elif b == c:
            height = (b**2 - (a/2)**2)**0.5
            area = (a * height) / 2
        else:
            height = (c**2 - (b/2)**2)**0.5
            area = (b * height) / 2
    elif (a**2 + b**2 == c**2):
        area = (a * b) / 2
    elif (b**2 + c**2 == a**2):
        area = (b * c) / 2
    elif (c**2 + a**2 == b**2):
        area = (c * a) / 2
    elif a != b and b != c and a != c:
        s = peri / 2
        height = 2*s*(s-a)*(s-b)*(s-c)
        if a != b:
            area = (c * height) / 2
        elif b != c:
            area = (a * height) / 2
        else:
            area = (b * height) / 2
    
    print("The area of the triangle is: ", area)

k = 'y'
while k == 'y' or k == 'Y':
    if check() == True:
        type()
        perimeter()
        area()
    k = input("Do you want to continue ?")
    

