import math

a = int(input('Podaj dlugosc jednego z boków: '))
b = int(input('Podaj długość drugiego boku: '))
c = math.sqrt(pow(a, 2)+pow(b, 2))
print(f"Przeciwprostokątna: {c}")
