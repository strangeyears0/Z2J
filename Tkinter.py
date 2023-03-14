# import tkinter as tk

# window = tk.Tk()
# greeting = tk.Label(
#     text = "Hello, Tkinter",
#     fg="white",
#     bg="#34A2AE",
#     width= 10,
#     height=10
# )
# greeting.pack()
# button = tk.Button(
#     text = "Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow"
# )
# button.pack()
# label = tk.Label(text = "Name")
# # entry = tk.Entry(fg = "yellow",bg="blue",width=50)
# entry = tk.Entry()
# name= entry.get()
# label.pack()
# entry.pack()

# text_box=tk.Text()
# text_box.pack()
# text_box.get("1.0")
# window.mainloop()

# frame = tk.Frame()
# frame.pack()
# window.mainloop()
# label = tk.Label(master=frame)

# import tkinter as tk
#
# window = tk.Tk()
#
# frame_a = tk.Frame()
#
#
# label_a = tk.Label(master=frame_a,text="I'm in Frame A")
# label_a.pack()
#
# frame_b = tk.Frame()
# label_b = tk.Label(master=frame_b,text="I'm in Frame B")
# label_b.pack()
#
# frame_a.pack()
# frame_b.pack()
#
# window.mainloop()


# ADJUSTING FRAME APPERANCE WITH RELIEFES:

# import tkinter as tk
#
# border_effects = {
#     "flat":tk.FLAT,
#     "sunken":tk.SUNKEN,
#     "raised":tk.RAISED,
#     "groove":tk.GROOVE,
#     "ridge":tk.RIDGE,
# }
#
# window = tk.Tk()
#
# for relief_name, relief in border_effects.items():
#     frame=tk.Frame(master=window,relief=relief,borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label= tk.Label(master=frame,text=relief_name)
#     label.pack()
# window.mainloop()

# ex2
#
# import tkinter as tk
# window = tk.Tk()
# button = tk.Button(
#     text="Click here",
#     width=50,
#     height=25,
#     bg="white",
#     fg="blue"
# )
# button.pack()
# window.mainloop()

# ex3
# import tkinter as tk
# window=tk.Tk()
# entry= tk.Entry(bg="white",fg="black",
#                 width=40)
# entry.insert(0,"What is your name?")
# entry.pack()
# window.mainloop()

#18.6 Controling layout with geometry

import tkinter as tk

# window=tk.Tk()
#
# frame1 = tk.Frame(master=window,width=100,height=100,bg="red")
# frame1.pack()
#
# frame2 = tk.Frame(master=window, width=50,height=50,bg="yellow")
# frame2.pack()
#
# frame3 = tk.Frame(master=window, width=25,height=25,bg="blue")
# frame3.pack()
#
# window.mainloop()

# import tkinter as tk
#
# window=tk.Tk()
#
# frame1 = tk.Frame(master=window,height=100,bg="red")
# frame1.pack(fill=tk.X)
#
# frame2 = tk.Frame(master=window,height=50,bg="yellow")
# frame2.pack(fill=tk.X)
#
# frame3 = tk.Frame(master=window,height=25,bg="blue")
# frame3.pack(fill=tk.X)
#
# window.mainloop()

# import tkinter as tk
#
# window=tk.Tk()
#
# frame1 = tk.Frame(master=window,width=200,height=100,bg="red")
# frame1.pack(fill=tk.Y,side=tk.LEFT,expand=True)
#
# frame2 = tk.Frame(master=window,width=100,bg="yellow")
# frame2.pack(fill=tk.Y,side=tk.LEFT,expand=True)
#
# frame3 = tk.Frame(master=window,width=50,bg="blue")
# frame3.pack(fill=tk.Y,side=tk.LEFT,expand=True)
#
# window.mainloop()
#
# import tkinter as tk
#
# window = tk.Tk()
#
# frame=tk.Frame(master=window,width=150,height=150)
# frame.pack()
#
# label1=tk.Label(master=frame,text="I'm at (0,0)",bg="red")
# label1.place(x=0,y=0)
#
# label2=tk.Label(master=frame,text="I'm at (75,75)",bg="yellow")
# label2.place(x=75,y=75)
#
# window.mainloop()

# import tkinter as tk
# window = tk.Tk()
# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j,padx=5,pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)
#
# window.mainloop()
#
import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()

