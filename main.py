import turtle

screen = turtle.Screen()
screen.title("US map")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


user_input = turtle.textinput("Enter state", "Geuss another state")



def on_click_on_screen(x, y):
    print(x, y)


turtle.onscreenclick(on_click_on_screen)

turtle.mainloop()
screen.exitonclick()
