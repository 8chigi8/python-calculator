def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Nie dzilimy przez zero!"

print("Wybierz operację:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielnie")

choice = input("Wybierz(1/2/3/4): ")

num1 = float(input("Wprowadz pierwszą liczbę: "))
num2 = float(input("Wprowadz drugą liczbę: "))

if choice == '1':
    print(f"Wynik: {add(num1, num2)}")
elif choice == '2':
    print(f"Wynik: {subtract(num1, num2)}")
elif choice == '3':
    print(f"Wynik: {multiply(num1, num2)}")
elif choice == '4':
    print(f"Wynik: {divide(num1, num2)}")
else:
    print("Nieprawidłowy wynik")
