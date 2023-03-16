import tkinter as tk

#create new window with title
window = tk.Tk()
window.title("Adress Entry Form")

#create a new frame frm_form to contain label
#and entry widgets for entering address info.

frm_form = tk.Frame(relief=tk.SUNKEN,borderwidth=3)
frm_form.pack()

#create a label and entry widgets for first name:
lbl_first_name = tk.Label(master=frm_form,text="First Name:")
ent_first_name = tk.Entry(master=frm_form,width=50)
#USe the grid geometry to place label and entry
lbl_first_name.grid(row=0,column=0,sticky="e")
ent_first_name.grid(row=0,column=1)

#create a label and entry widg for last name
lbl_last_name = tk.Label(master=frm_form,text="Last Name:")
ent_last_name =  tk.Entry(master= frm_form,width=50)
#place widget i the second row
lbl_last_name.grid(row=1,column=0,sticky="e")
ent_last_name.grid(row=1,column=1)

#create a label and entry widg for adress line 1
lbl_address1 = tk.Label(master=frm_form,text="Address Line 1:")
ent_address1 = tk.Entry(master=frm_form,width=50)
#place widget in third row
lbl_address1.grid(row=2,column=0,sticky="e")
ent_address1.grid(row=2,column=1)


#create a label and entry widg for adress line 2
lbl_address2 = tk.Label(master=frm_form,text="Address Line 2:")
ent_address2 = tk.Entry(master=frm_form,width=50)
#place widget in fourth row
lbl_address2.grid(row=3,column=0,sticky="e")
ent_address2.grid(row=3,column=1)


#create a label and entry wdg for city
lbl_city = tk.Label(master=frm_form,text="City:")
ent_city = tk.Entry(master=frm_form,width=50)
#place widget in fifth row
lbl_city.grid(row=4,column=0,sticky="e")
ent_city.grid(row=4,column=1)

# Create the Label and Entry widgets for "State/Province"
lbl_state = tk.Label(master=frm_form, text="State/Province:")
ent_state = tk.Entry(master=frm_form, width=50)
# Place the widgets in the sixth row of the grid
lbl_state.grid(row=5, column=0, sticky=tk.E)
ent_state.grid(row=5, column=1)

# Create the Label and Entry widgets for "Postal Code"
lbl_postal_code = tk.Label(master=frm_form, text="Postal Code:")
ent_postal_code = tk.Entry(master=frm_form, width=50)
# Place the widgets in the seventh row of the grid
lbl_postal_code.grid(row=6, column=0, sticky=tk.E)
ent_postal_code.grid(row=6, column=1)

# Create the Label and Entry widgets for "Country"
lbl_country = tk.Label(master=frm_form, text="Country:")
ent_country = tk.Entry(master=frm_form, width=50)
# Place the widgets in the eight row of the grid
lbl_country.grid(row=7, column=0, sticky=tk.E)
ent_country.grid(row=7, column=1)
# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

# Start the application

window.mainloop()
