# importing the tkinter library 
from tkinter import *
# variables to store x cordinate in current_x and y cordiinate in current_y
current_x, current_y = 0, 0
# when to drag the mouse we craete the variable color to make our mouse drag visible 
color = "black"


# this function is basically for the cordinates whenever user is going to click on the screen 
# we will get the cordinates in the output screen and that is lacated in the variables 
def locate_xy(event):
    global current_x, current_y
    current_x, current_y = event.x, event.y


# this function to drag the mouse on to the canvas but when we evoke the create line fuction this will make the starting point same 
# so for that we need to update the current x and current y variables and we updated it in last line and for some color to show we added color variable 
def addLine(event):
    global current_x, current_y
    canvas.create_line((current_x, current_y, event.x, event.y),fill= color)
    current_x,current_y =event.x, event.y


# this function basically runs the color or assigns that color to which he user clicks 
def show_color(new_color):
    global color
    color = new_color


# this function is created so that it deletes all the content from the canvas and creates a new one and again display the pallate 
def new_canvas():
    canvas.delete("all")
    display_pallete()


# creating the window 
window = Tk()
# giving window the title using title 
window.title("Paint")
# to make the make full screen use state 
window.state("zoomed")
# to make the background color 
window.config(bg="blue")
# to make the grid we are using the row and column configure 
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# in this part we are going to create a menu and a menubar where we can have several options for our paint 
menubar = Menu(window)
window.config(menu = menubar)
# this creates the submenu part 
submenu = Menu(menubar,tearoff=0)
# this craetes a menu and a submenu file and a new canvas using built in functions add cascase and add command 
menubar.add_cascade(label = "File", menu=submenu)
submenu.add_command(labe="New Canvas", command=new_canvas)


# canvas is created as we are going to place it on our window having white background 
canvas = Canvas(window, background="white")
# to make the canvas full screen nsew-->north south east west so it is going to be in all directions 
canvas.grid(row=0, column=0, sticky="nsew")
# we use bind function when user is going to click on the window the function locate_xy activates 
canvas.bind("<Button-1>", locate_xy)
# another bind is when user is going to drag the mouse on the canvas addline function is going to evoke 
canvas.bind("<B1-Motion>", addLine)


# this function creates the color palette and colors are the shown in the rectangle boxes and that is stored in a id 
# and to make that color run on canvas we have to bind that color to the id 
# the first parameter is id then the button that whenver user clicks it it runs that color and lambda
#  function calling show_color function which actually runs that color and apply this to all color 
def display_pallete():
    id=canvas.create_rectangle((10,10,30,30),fill="black")
    canvas.tag_bind(id,"<Button-1>",lambda x: show_color("black"))
    id=canvas.create_rectangle((10,40,30,60),fill="gray")
    canvas.tag_bind(id,"<Button-1>",lambda x: show_color("gray"))
    id=canvas.create_rectangle((10,70,30,90),fill="brown4")
    canvas.tag_bind(id,"<Button-1>",lambda x: show_color("brown4"))
    id=canvas.create_rectangle((10,100,30,120),fill="blue")
    canvas.tag_bind(id,"<Button-1>",lambda x: show_color("blue"))
    id=canvas.create_rectangle((10,130,30,150),fill="green")
    canvas.tag_bind(id,"<Button-1>",lambda x: show_color("green"))
    id=canvas.create_rectangle((10,160,30,180),fill="red")
    canvas.tag_bind(id,"<Button-1>",lambda x: show_color("red"))
    id=canvas.create_rectangle((10,190,30,210),fill="purple")
    canvas.tag_bind(id,"<Button-1>",lambda x: show_color("purple"))
    id=canvas.create_rectangle((10,220,30,240),fill="orange")
    canvas.tag_bind(id,"<Button-1>",lambda x: show_color("orange"))
    window.mainloop()

# calling this  function will display the pallete again and we have our canvas ready 
display_pallete()

