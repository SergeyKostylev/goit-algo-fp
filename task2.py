import sys
import turtle

NEXT_LENGTH_COEFFICIENT = 0.75
ANGLE = 45

def draw_branch(t, branch_length, depth):
    if depth == 0:
        return
    t.forward(branch_length)

    position = t.position()
    heading = t.heading()

    t.left(ANGLE)
    draw_branch(t, branch_length * NEXT_LENGTH_COEFFICIENT, depth - 1)

    t.setposition(position)
    t.setheading(heading)

    t.right(ANGLE)
    draw_branch(t, branch_length * NEXT_LENGTH_COEFFICIENT, depth - 1)

    t.setposition(position)
    t.setheading(heading)


def pythagoras_tree(t, branch_length, depth):
    if depth == 0:
        return

    for _ in range(4):
        t.forward(branch_length)
        t.left(90)

    t.forward(branch_length)
    t.left(ANGLE)

    new_length = branch_length // 2

    pythagoras_tree(t, new_length, depth - 1)

    t.right(90)
    t.forward(new_length)

    pythagoras_tree(t, new_length, depth - 1)

    t.left(45)
    t.backward(branch_length)

if __name__ == '__main__':
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    window = turtle.Screen()
    window.getcanvas().winfo_toplevel().geometry("+0+100")
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)

    draw_branch(t, 100, depth)

    window.mainloop()
