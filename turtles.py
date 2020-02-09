import turtle

def main():
    window = turtle.Screen()
    victor = turtle.Turtle()

    make_square(victor)

    turtle.mainloop()

def make_square(victor):
    length = int(input('Square size: '))

    for i in range(4):
        make_line_and_turn(victor, length)

def make_line_and_turn(victor, length):
    victor.forward(length)
    victor.left(90)

if __name__ == '__main__':
    main()