from graphical_interface.graphical import *
from gamesettings import *

def main(page: ft.Page):
    page.title = "Tic Tac Toe"
    page.update()
    ttt = TicTacToe()
    page.add(ttt)

ft.app(target=main)