# import tkinter as tk
#
# #create a window object
#
# window = tk.Tk()
#
# #Assume this list gets updated automatically
# events_list = []
#
# #Create an event handler
#
# def handle_keypress(event):
#     """Print the characetr associated to the key pressed"""
#     print(event.char)
#
#
#
# #Run the event loop
#
# while True:
#     #If events_list is empty, then no events have occurred and you
#     #can skip to tehe next iteration of the loop
#     if events_list ==[]:
#         continue
#     # if execution reaches this point then at last one
#     #     event object in event_list
#     event=events_list[0]
#
#     #if event is a keypress event object
#     if event.type == "keypress":
#         handle_keypress(event)
#
# window.mainloop()

# import tkinter as tk
#
# window = tk.Tk()
#
# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)
#
# # Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)
#
#
#
# def handle_click(event):
#     print("The button was clicked!")
#
# button = tk.Button(text="Click me!")
# button.pack()
#
# button.bind("<Button-1>", handle_click)
#
# window.mainloop()


import tkinter as tk

def incrase():
    value = int(lbl_value["text"])
    lbl_value["text"]=f"{value+1}"


def decrase():
    value = int(lbl_value["text"])
    lbl_value["text"]=f"{value-1}"

window = tk.Tk()

window.rowconfigure(0,minsize=50, weight=1)
window.columnconfigure([0,1,2],minsize=50,weight=1)

btn_decrase = tk.Button(master=window, text ="-",command=decrase)
btn_decrase.grid(row=0,column=0,sticky="nsew")

lbl_value=tk.Label(master=window,text="0")
lbl_value.grid(row=0,column=1)

btn_incrase = tk.Button(master=window,text="+",command=incrase)
btn_incrase.grid(row=0,column=2,sticky="nsew")

window.mainloop()