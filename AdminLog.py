from tkinter import *
from tkinter import messagebox
def pizza_software():
	window = Toplevel()
	def process(pizza_type,pizza_size,beverage_type,beverage_size):
		message1 = messagebox.askyesno("Confirm" , "Is this your final order?")
		# the calculation
		if message1 == 1:
			Price = LabelFrame(window, text = "Bill" , padx = 30 , pady = 25 )
			Price.grid(row = 2 , column = 0)
			price = {"Peporoni Pizza" : 100 , "Cheese Pizza" : 125 , "Veg-Pizza" : 75 , "Coke" : 25 , "Limca" : 35 , "Pepsi" : 40}
			size = {"Large " : 3 , "Medium " : 2 , "Small " : 1 , "Large" : 3 , "Medium" : 2 , "Small" : 1}
			price_1 = Label(Price , text = (pizza_size + pizza_type + " and " + beverage_size + beverage_type), bg = "Yellow")
			price_1.grid(row = 0 , column = 0  , sticky = EW)
			price_2 = Label(Price , text = ("Pizza : " + str(price[pizza_type] * size[pizza_size]) + " and " + "Beverage : " + str(price[beverage_type] * size[beverage_size])), bg = "Yellow")
			price_2.grid(row = 1 , column = 0 , sticky = EW)
			final_price = Label(Price , text = ("Total : " + str( price[pizza_type] * size[pizza_size] + price[beverage_type] * size[beverage_size])), bg = "Yellow")
			final_price.grid(row = 2 , column = 0 , sticky = EW)

	window.title("Bill maker")


	# Defining The Radio Buttons
	pizza_type = StringVar()
	pizza_type.set(0)
	a = LabelFrame(window, text = "Pizza Type" , padx = 30 , pady = 25 )
	a.grid(row = 0 , column = 0, padx = 35 , pady = 30)
	Radiobutton(a, text = "Peporoni Pizza" , variable = pizza_type , value = "Peporoni Pizza",bg = "#AAFFAA", fg = "Black").grid(row = 0 , column = 0, sticky = EW)
	Radiobutton(a, text = "Cheese Pizza" , variable = pizza_type , value = "Cheese Pizza",bg = "#AAFFAA", fg = "Black").grid(row = 1 , column = 0, sticky = EW)
	Radiobutton(a, text = "Veg-Pizza" , variable = pizza_type , value = "Veg-Pizza",bg = "#AAFFAA", fg = "Black").grid(row = 2 , column = 0, sticky = EW)

	pizza_size = StringVar()
	pizza_size.set(0)
	b = LabelFrame(window, text = "Pizza Size" , padx = 30 , pady = 25 )
	b.grid(row = 0 , column = 1, padx = 35 , pady = 30)
	Radiobutton(b, text = "Large" , variable = pizza_size , value = "Large " ,bg = "#FFAAAA", fg = "Black").grid(row = 0 , column = 0, sticky = EW)
	Radiobutton(b, text = "Medium" , variable = pizza_size , value = "Medium ",bg = "#FFAAAA", fg = "Black").grid(row = 1 , column = 0, sticky = EW)
	Radiobutton(b, text = "Small" , variable = pizza_size , value = "Small ",bg = "#FFAAAA", fg = "Black").grid(row = 2 , column = 0, sticky = EW)

	beverage_type = StringVar()
	beverage_type.set(0)
	c = LabelFrame(window, text = "Beverage Type" , padx = 30 , pady = 25 )
	c.grid(row = 0 , column = 2, padx = 35 , pady = 30)
	Radiobutton(c, text = "Coke" , variable = beverage_type , value = "Coke",bg = "#AAAAFF", fg = "Black").grid(row = 0 , column = 0, sticky = EW)
	Radiobutton(c, text = "Limca" , variable = beverage_type , value = "Limca",bg = "#AAAAFF", fg = "Black").grid(row = 1 , column = 0, sticky = EW)
	Radiobutton(c, text = "Pepsi" , variable = beverage_type , value = "Pepsi",bg = "#AAAAFF", fg = "Black").grid(row = 2 , column = 0, sticky = EW)

	beverage_size = StringVar()
	beverage_size.set(0)
	d = LabelFrame(window, text = "Beverage Size" , padx = 30 , pady = 25 )
	d.grid(row = 0 , column = 3, padx = 35 , pady = 30)
	Radiobutton(d, text = "Large" , variable = beverage_size , value = "Large",bg = "#856ff8", fg = "Black").grid(row = 0 , column = 0, sticky = EW)
	Radiobutton(d, text = "Medium" , variable = beverage_size , value = "Medium",bg = "#856ff8", fg = "Black").grid(row = 1 , column = 0, sticky = EW)
	Radiobutton(d, text = "Small" , variable = beverage_size , value = "Small",bg = "#856ff8", fg = "Black").grid(row = 2 , column = 0, sticky = EW)


	#Making the submit button
	button = Button(window, text = "Submit" ,bg = "Black" , fg = "White", command = lambda : process(pizza_type.get(),pizza_size.get(),beverage_type.get(),beverage_size.get()))
	button.grid(row = 1 , column = 0 , columnspan = 4)









def check(name , password , dir):
	name = name.lower()
	if name not in dir:
		warn = messagebox.showerror("Invalid Username" , "Unknow User")
	elif dir[name] != password:
		warn = messagebox.showerror("Invalid Password" , "Incorrect Password")
	else:
		Label( log , text = "Welcome").grid( columnspan = 2 , row = 3 , column = 0 )
		pizza_software()

root1 = Tk()

directory = {"krish" : "1234"}

log = LabelFrame(root1, text = "Administrator Login",padx = 100 , pady = 50)
log.grid(row = 1 , column = 1)

Label(log , text = "Username : ").grid(row = 0 , column = 0)

Label(log , text = "Password : ").grid(row = 1 , column = 0)

name = Entry(log , width = 20)
name.grid(row = 0 , column = 1)

password = Entry(log , width = 20 , show = "*")
password.grid(row = 1 , column = 1)

button = Button( log , text = "Login" , command = lambda : check(name.get() , password.get() , directory))
button.grid(columnspan =  2,row = 2 , column =0 , sticky = EW)
root1.mainloop()
