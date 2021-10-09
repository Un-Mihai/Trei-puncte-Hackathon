import turtle
t2 = turtle.Turtle()
t = turtle.Turtle()
s = turtle.getscreen()
d = 20
t2.speed(0)

def dreptunghi(x, y, l, L, c, fc):
    t.color(c)
    t.fillcolor(fc)
    t.pu()
    t.goto(x, y)
    t.begin_fill()
    t.pd()
    for i in range(2):
        t.fd(l)
        arcs()
        t.fd(L)
        arcs()
    t.end_fill()

def telefon(x, y, l, L, c, fc, dott):
    t.color(c)
    t.fillcolor(c)
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    for j in range(2):
        t.fd(l)
        arcs()
        t.fd(L)
        arcs()
    t.end_fill()
    dreptunghi(-25/2*d+5, -5*d+30, l-10, L-35, "purple", "white")
    t.pu()
    t.goto(-25/2*d+50, -5*d+15)
    t.pd()
    t.color("white")
    t.dot(dott)

def arcd():
    t2.rt(180)
    t2.circle(d,-90)
    t2.rt(180)

def arcs():
    t2.circle(d,90)

t2.pencolor("blue")
t2.pu()
t2.goto((3.5*d),(-19.5*d))
t2.pd()
t2.lt(90)
t2.fd(5*d)
arcd()
t2.fd(2*d)
arcs()
t2.fd(5*d)
arcd()
t2.fd(3*d)

#aici punem telefon

t2.fd(-2*d)
t2.rt(-90)
t2.fd(4*d)

#aici punem telefon

t2.pu()
t2.rt(90)
t2.fd(1.5*d)
t2.rt(-90)
t2.fd(2*d)
t2.rt(90)
t2.pd()
t2.fd(5.5*d)

#aici punem tableta

t2.pu()
t2.fd(2*d)
t2.rt(-90)
t2.fd(2*d)
t2.pd()
t2.fd(3*d)

#aici punem telefon

t2.pencolor("green")
t2.pu()
t2.goto((4.5*d),(-19.5*d))
t2.pd()
t2.fd(6*d)

t2.pencolor("#237F9E")
t2.pu()
t2.goto((2.5*d),(-19.5*d))
t2.pd()
t2.fd(9*d)
arcd()
t2.fd(3*d)
arcs()

t2.pencolor("#BFBA2C")
t2.pu()
t2.goto(2.5*d,-10.5*d)
t2.pd()
t2.fd(3*d)
arcd()
t2.fd(d)
arcs()
t2.fd(3*d)

t2.pencolor("#CC8B12")
t2.pu()
t2.goto((1.5*d),(-19.5*d))
t2.pd()
t2.fd(17*d)
