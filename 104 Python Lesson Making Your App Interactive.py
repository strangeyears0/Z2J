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

import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)



def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()
