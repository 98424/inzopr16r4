print("Hello World")
def dodawanie(a, b):
	return a+b
try:
	a = int(input("Podaj 1 liczbe"))
	b = int(input("Podaj 2 liczbe"))
	print(dodawanie(a,b))
except ValueError as ve:
	print("Wprowadzono bledne dane, koniec..")
print(dodawanie(a,b))
input()
