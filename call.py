from Calc import Addition
from Calc import Subtraction
from Calc import Multiplication
from Calc import Division
from Calc import Exponentiation
from Calc import Mode

a = int(input("Enter your First Number: "))
b = int(input("Enter your Second NUmber: "))

print(f'{a} and {b} addititon value is : ', Addition.value(a,b))
print(f'{a} and {b} addititon value is : ', Subtraction.value(a,b))
print(f'{a} and {b} addititon value is : ', Multiplication.value(a,b))
print(f'{a} and {b} addititon value is : ', Division.value(a,b))
print(f'{a} and {b} addititon value is : ', Mode.value(a,b))
print(f'{a} and {b} addititon value is : ', Exponentiation.value(a,b))