
def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return "Błąd: Dzielenie przez zero"
    return a / b

def kalkulator():
    print("Prosty kalkulator w Pythonie")
    print("Dostępne operacje:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")
    
    while True:
        wybor = input("Wybierz operację (1-5): ")
        
        if wybor == '5':
            print("Do widzenia!")
            break
        
        try:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
            
            if wybor == '1':
                print(f"Wynik: {dodawanie(a, b)}")
            elif wybor == '2':
                print(f"Wynik: {odejmowanie(a, b)}")
            elif wybor == '3':
                print(f"Wynik: {mnozenie(a, b)}")
            elif wybor == '4':
                print(f"Wynik: {dzielenie(a, b)}")
            else:
                print("Nieprawidłowy wybór!")
        except ValueError:
            print("Błąd: Wprowadź poprawne liczby")

if __name__ == "__main__":
    kalkulator()
