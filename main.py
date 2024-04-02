from graphical_interface.graphical import TicTacToeWindow
from gamesettings.game import TicTacToe
from flet import Page, app


def main(page: Page):
    page.title = "Tic Tac Toe"
    # create application instance
    tctcte = TicTacToeWindow()
    # add application's root control to the page
    page.add(tctcte)


if __name__ == "__main__":
    app(target=main)
