import flet as ft
from gamesettings import game


ttt = game.TicTacToe()


class TicTacToeWindow(ft.UserControl):
    def build(self):
        self.winner = "Fim!"
        result = ft.Text(value="TIC TAC TOE", color=ft.colors.WHITE, size=40)
        self.dlg = ft.AlertDialog(
            title=ft.Text(f"{self.winner}"), on_dismiss=lambda e: print("Fim!")
        )
        return ft.Container(
            width=600,
            height=600,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment="center"),
                    ft.Container(
                      height=200
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text=f"{ttt.get_board()[0][0]}",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button,
                                data=[0, 0]
                            ),
                            ft.ElevatedButton(
                                text=f"{ttt.get_board()[0][1]}",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button,
                                data=[0, 1]
                            ),
                            ft.ElevatedButton(
                                text=f"{ttt.get_board()[0][2]}",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button,
                                data=[0, 2]
                            ),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text=f"{ttt.get_board()[1][0]}",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button,
                                data=[1, 0]
                            ),
                            ft.ElevatedButton(
                                text=f"{ttt.get_board()[1][1]}",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button,
                                data=[1, 1]
                            ),
                            ft.ElevatedButton(
                                text=f"{ttt.get_board()[1][2]}",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button,
                                data=[1, 2]
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text=f"{ttt.get_board()[2][0]}",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button,
                                data=[2, 0],
                            ),
                            ft.ElevatedButton(
                                text=f"{ttt.get_board()[2][1]}",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button,
                                data=[2, 1]
                            ),
                            ft.ElevatedButton(
                                text=f"{ttt.get_board()[2][2]}",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                                on_click=self.button,
                                data=[2, 2]
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[self.dlg], alignment="center",
                    )
                ]
            )
        )

    def button(self, e):
        data = e.control.data
        mark = ttt.rungame(data)
        if e.control.text == "_":
            e.control.text = mark
        else:
            pass
        if ttt.check_win()[0]:
            self.winner = ttt.announce_winner()
            self.open_dlg()
        self.update()

    def open_dlg(self):
        self.dlg.open = True
        self.update()
