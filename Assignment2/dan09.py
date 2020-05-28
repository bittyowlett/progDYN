import numpy as np
import turtle as turtle

paramSet = [np.e, 0.5*(1+np.sqrt(5)), np.log(2), np.pi, 4.66920169102990, np.euler_gamma]
nameSet = [("(a)   [s={}]").format(paramSet[0]), 
           ("(b)   [s={}]").format(paramSet[1]), 
           ("(c)   [s={}]").format(paramSet[2]),
           ("(d)   [s={}]").format(paramSet[3]),
           ("(e)   [s={}]").format(paramSet[4]),
           ("(f)   [s={}]").format(paramSet[5])]

def f_eta(eta_n, s):
    return np.fmod(eta_n + 2*np.pi*s, 2*np.pi)

def f_phi(phi_n, eta_n): 
    return np.fmod(eta_n + phi_n, 2*np.pi)

phi_0 = 0
eta_0 = 0
unitSet = [10, 10, 10, 10, 10, 10] # unit lengths for (a), (b), (c) etc. in pixel
speedSet = [0, 0, 0, 0, 0, 0]  # "fastest, no animation"=0; "fast"=10, "normal"=6, "slow"=3, "slowest"=1
iterationSet = [6000, 6000, 6000, 6000, 6000, 6000]


turtle.title("Fractals with Turtle in Python")
turtle.getscreen().bgcolor("black")
turtle.color("white", "red")
turtle.pensize(1)
turtle.setundobuffer(None)
turtle.hideturtle()
turtle.radians()
turtle.getscreen().delay(0)


for i in range(6):
    phi_n = phi_0
    eta_n = eta_0
    
    turtle.title("Drawing... Fractal " + nameSet[i])
    turtle.speed(speedSet[i])
    
    for iteration in np.arange(iterationSet[i]):
        if phi_n >= 0:
            turtle.left(phi_n)
        else:
            turtle.right(np.abs(phi_n))
        turtle.forward(unitSet[i])
        eta_n = f_eta(eta_n, paramSet[i])
        phi_n = f_phi(phi_n, eta_n)
        
    turtle.clear()
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.pendown()
