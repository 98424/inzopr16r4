
def dodawanie(a, b):
	return a+b
	
def get_info():
	return "To jest program kalkulator stworzony przez Mateusza"
try:
	a = int(input("Podaj 1 liczbe"))
	b = int(input("Podaj 2 liczbe"))
	print(dodawanie(a,b))
except ValueError as ve:
	print("Wprowadzono bledne dane, koniec..")
	
print(get_info())
input()
