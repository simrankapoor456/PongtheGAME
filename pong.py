import turtle

gamewindow = turtle.Screen()
gamewindow.title("Pong the GAME")
gamewindow.bgcolor("darkblue")
gamewindow.setup(width=800, height=500)
gamewindow.tracer(0) #stops the window from updating, so we've to manually update the game, this helps us to speed up the game

#checking if everything is working fine or not

print("Testing")
#Main Game Loop
while True:
    gamewindow.update()