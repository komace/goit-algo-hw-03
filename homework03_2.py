import turtle

def koch_snowflake(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        koch_snowflake(t, length, depth - 1)
        t.left(60)
        koch_snowflake(t, length, depth - 1)
        t.right(120)
        koch_snowflake(t, length, depth - 1)
        t.left(60)
        koch_snowflake(t, length, depth - 1)

def draw_snowflake(t, length, depth):
    for _ in range (3):
        koch_snowflake(t, length, depth)
        t.right(120)

def main():
    # Встановлюємо параметри вікна черепашки
    screen = turtle.Screen()
    screen.setup(width=800, height = 600)
    screen.bgcolor("white")

    # Створюємо об'єкт черепашки
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Запитуємо у користувача рівень рекурсії
    depth = int(input("Введіть рівень рекурсії: "))

    # Намалювати сніжинку Коха
    draw_snowflake(t, 400, depth)

    turtle.done()

if __name__ == "__main__":
    main()    



