import random

def run():
    find_number = False
    random_number = random.randint(0,20)

    while not find_number:
        inputNumber = int(input("Ingresa un número del 0 al 19: "))

        if inputNumber == random_number:
            print("Felicitaciones! Encontraste el número")
            find_number = True
        elif inputNumber > random_number:
            print("El número es menor")
        else:
            print("El número es mayor")

if __name__ == "__main__":
    run()