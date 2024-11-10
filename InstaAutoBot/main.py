import os
import flet as ft
import webbrowser  # Importando o módulo para abrir o navegador

def main(page: ft.Page):
    page.title = "InstaAutoBot"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.window.bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT
    page.window.title_bar_hidden = True

    # Configurações da janela
    page.window.maximizable = False
    page.window.minimizable = False
    page.window.width = 600
    page.window.height = 1050
    page.window.max_width = 600
    page.window.max_height = 1050
    page.window.min_width = 600
    page.window.min_height = 1050

    # Função para abrir o site
    def open_website(e):
        webbrowser.open("https://flet.dev/")  # Altere a URL para o site que você deseja abrir

    # Configurando o appbar com o botão "INFO" que abre o site
    page.appbar = ft.CupertinoAppBar(
        leading=ft.IconButton(ft.icons.INFO, icon_color=ft.colors.WHITE, on_click=open_website),  # Adicionando o evento de clique
        bgcolor="#7834bf",
        trailing=ft.IconButton(ft.icons.CLOSE, icon_color=ft.colors.WHITE),
    )

    # Adicionando um container com uma imagem como background
    background = ft.Container(
        width=600,
        height=1050,
        margin=ft.margin.all(-10),
        image_src=os.path.join("InstaAutoBot", "assets", "img", "background.png"),
        image_fit=ft.ImageFit.COVER,
        alignment=ft.alignment.center,  # Centraliza o conteúdo dentro do container
        content=ft.Column(
            [
                ft.Text("Best engagement bot for", 
                        offset=ft.Offset(x=0, y=-2.5),
                        size=40, 
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                ),

                ft.Text("Instagram",
                        offset=ft.Offset(x=0, y=-2.5),
                        size=40, 
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                ),

                ft.Image(
                        src=os.path.join("InstaAutoBot", "assets", "img", "bot.png"),
                        width=300,
                        height=300,
                        fit=ft.ImageFit.CONTAIN,
                ),

                ft.Text("Nice to meet you!",
                        color=ft.colors.WHITE,
                        offset=ft.Offset(x=0, y=0.1),
                        size=25,
                        weight=ft.FontWeight.BOLD,
                ),

                ft.Text("Log in to Instagram first, then click the", 
                        color=ft.colors.WHITE,
                        offset=ft.Offset(x=0, y=1),
                        size=25,
                ),

                ft.Text("button below!",
                        color=ft.colors.WHITE,
                        offset=ft.Offset(x=0, y=1),
                        size=25,
                ),

                ft.ElevatedButton("Start Automation",
                                  style=ft.ButtonStyle(
                                      text_style=ft.TextStyle(size=34, weight=ft.FontWeight.BOLD),
                                  ),
                                  offset=ft.Offset(x=0, y=1), 
                                  bgcolor=ft.colors.WHITE, 
                                  color=ft.colors.BLACK,
                                  width=450,
                                  height=80
                )
            ],
            alignment="center",  # Centraliza os itens dentro da coluna
            horizontal_alignment="center",  # Centraliza horizontalmente
        )
    )

    # Centraliza o próprio container dentro da página
    page.add(
        ft.Container(
            content=background,
            alignment=ft.alignment.center,  # Centraliza o container de background na página
        )
    )

ft.app(main)