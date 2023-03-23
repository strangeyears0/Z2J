import tkinter as tk
import random
def rock():

    choice=(1,2,3)
    random_choice=random.choice(choice)
    player_choice=1
    if random_choice == player_choice:
        window_draw=tk.Tk()
        window_draw.title("DRAW")
        window_draw_lbl=tk.Label(window_draw,text="You Choose Rock\nPC Choose Rock\nDraw")
        window_draw_lbl.grid(row=0,column=0)
    elif  random_choice == 2:

        window_lose = tk.Tk()
        window_lose.title("LOSE")
        window_lose_lbl=tk.Label(window_lose,text="You Choose Rock\nPC Choose Paper\nYou Lose")
        window_lose_lbl.grid(row=0,column=0)

    else:
        window_win= tk.Tk()
        window_win.title("Win")
        window_win_lbl=tk.Label(window_win,text="You Choose Rock\nPC Choose Scissors\nYou Win")
        window_win_lbl.grid(row=0,column=0)

def paper():

    choice=(1,2,3)
    random_choice=random.choice(choice)
    player_choice=2
    if random_choice == player_choice:
        window_draw=tk.Tk()
        window_draw.title("DRAW")
        window_draw_lbl=tk.Label(window_draw,text="You Choose Paper\nPC Choose Paper\nDraw")
        window_draw_lbl.grid(row=0,column=0)
    elif  random_choice == 1:

        window_lose = tk.Tk()
        window_lose.title("WIN")
        window_lose_lbl=tk.Label(window_lose,text="You Choose Paper\nPC Choose Rock\nYou Win")
        window_lose_lbl.grid(row=0,column=0)

    else:
        window_win= tk.Tk()
        window_win.title("LOSE")
        window_win_lbl=tk.Label(window_win,text="You Choose Paper\nPC Choose Scissors\nYou Lose")
        window_win_lbl.grid(row=0,column=0)

def scissors():

    choice=(1,2,3)
    random_choice=random.choice(choice)
    player_choice=3
    if random_choice == player_choice:
        window_draw=tk.Tk()
        window_draw.title("DRAW")
        window_draw_lbl=tk.Label(window_draw,text="You Choose Scissors\nPC Choose Scissors\nDraw")
        window_draw_lbl.grid(row=0,column=0)
    elif  random_choice == 1:

        window_lose = tk.Tk()
        window_lose.title("LOSE")
        window_lose_lbl=tk.Label(window_lose,text="You Choose Scissors\nPC Choose Rock\nYou Lose")
        window_lose_lbl.grid(row=0,column=0)

    else:
        window_win= tk.Tk()
        window_win.title("WIN")
        window_win_lbl=tk.Label(window_win,text="You Choose Scissors\nPC Choose Paper\nYou Win")
        window_win_lbl.grid(row=0,column=0)
def one_player():
    game_window["text"]="Choose your weapon!"
    game_btn_frame=tk.Frame(game_window,relief=tk.RAISED)
    btn_rock = tk.Button(game_btn_frame,text="Rock",command=rock)
    btn_rock.grid(row=0,column=0)
    btn_paper = tk.Button(game_btn_frame,text="Paper",command=paper)
    btn_paper.grid(row=0,column=1)
    btn_scissors = tk.Button(game_btn_frame,text="Scissors",command=scissors)
    btn_scissors.grid(row=0,column=3)
    game_btn_frame.grid(row=1,column=0)


window = tk.Tk()
window.title("Rock Paper Scissors")

window.rowconfigure(0,minsize=100,weight=1)
window.columnconfigure(1,minsize=100,weight=1)

game_window = tk.Label(window)
game_window.rowconfigure(0,weight=3)
game_window.columnconfigure(0,weight=3)
fr_buttons = tk.Frame(window,relief=tk.RAISED,bd=2)
btn_player1 = tk.Button(fr_buttons,text="1 Player",command=one_player)
# btn_player2 = tk.Button(fr_buttons,text="2 Player")

btn_player1.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
# btn_player2.grid(row=1,column=0,sticky="ew",padx=5,pady=5)
fr_buttons.grid(row=0,column=0,sticky="ns")
game_window.grid(row=0,column=1,sticky="nsew")
window.mainloop()

