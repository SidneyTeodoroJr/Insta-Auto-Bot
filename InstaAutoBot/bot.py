import os
import time
import random
import pyautogui as pg
from pyautogui import ImageNotFoundException
import webbrowser as web
from pynput import keyboard
import tkinter as tk
from tkinter import messagebox
from modules.image_search import ImageLocator

# Variável global que controla a execução do bot
running = True

# Caminho do arquivo de comentários
comments_path = os.path.join("InstaAutoBot", "comments.txt")

# Função para carregar comentários do arquivo comments.txt
def carregar_comentarios():
    try:
        with open(comments_path, "r", encoding="utf-8") as file:
            comentarios = [linha.strip() for linha in file if linha.strip()]
        return comentarios
    except FileNotFoundError:
        print("Erro: O arquivo 'comments.txt' não foi encontrado.")
        return []

def main_bot():
    global running
    comentarios = carregar_comentarios()

    if not comentarios:
        print("Nenhum comentário disponível. Verifique o arquivo 'comments.txt'.")
        return

    # Criando a janela tkinter
    root = tk.Tk()
    root.withdraw()  # Mantém a janela oculta inicialmente

    def on_press(key):
        global running
        if key == keyboard.Key.esc:
            print("Tecla ESC pressionada!")
            print("Bot interrompido.")
            running = False
            return False  

    def bot_run():
        global running
        messagebox.showinfo("AVISO", "Para interromper a automação, aperte 'ESC' no teclado.")

        url = "https://www.instagram.com/"
        web.open(url)

        pg.sleep(10)
        pg.hotkey("ctrl", "0")
        pg.sleep(1)
        
        def bot_seta():
            image_path = os.path.join("InstaAutoBot", "assets","img-steps", "seta.png")
            try:
                home_position = pg.locateCenterOnScreen(image_path, confidence=0.8)
                if home_position:
                    pg.moveTo(home_position, duration=1)
                    pg.leftClick()
                    time.sleep(1.5)
                    pg.hotkey("f11")
            except ImageNotFoundException:
                print("Elemento não encontrado.")
                messagebox.showerror("ERRO", "Elemento não encontrado!")
                pg.sleep(1.5)
                messagebox.showinfo("AVISO", "Automação do Instagram, encerrada!")
                pg.hotkey("esc")

        bot_seta()

        def bot_click_like():
            imagens = [
                os.path.join("InstaAutoBot", "assets", "img-steps", "msg_alerta_light.png"), 
                os.path.join("InstaAutoBot", "assets", "img-steps", "msg_alerta_dark.png"),

                os.path.join("InstaAutoBot", "assets", "img-steps", "seguir_light.png"),
                os.path.join("InstaAutoBot", "assets", "img-steps", "seguir_dark.png"),

                os.path.join("InstaAutoBot", "assets", "img-steps", "like_light.png"),
                os.path.join("InstaAutoBot", "assets", "img-steps", "like_dark.png"),

                os.path.join("InstaAutoBot", "assets", "img-steps", "cancel_light.png"),
                os.path.join("InstaAutoBot", "assets", "img-steps", "cancel_dark.png"),

                os.path.join("InstaAutoBot", "assets", "img-steps", "comment_light.png"),
                os.path.join("InstaAutoBot", "assets", "img-steps", "comment_dark.png")
            ]

            time.sleep(0.1)
            for img_path in imagens:
                if "seguindo_light.png" in img_path or "seguindo_dark.png" in img_path:
                    print(f"Ignorando a imagem: {img_path}")
                    continue

                locator = ImageLocator(img_path)
                locator.start_search()
                time.sleep(0.1)

        def like_loop():
            global running
            while running:
                bot_click_like()

                comentario_escolhido = random.choice(comentarios)
                pg.write(comentario_escolhido, interval=0.1)
                pg.sleep(2)
                pg.hotkey("enter")

                pg.sleep(5)
                pg.scroll(-500)
                time.sleep(0.1)

        like_loop()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    bot_run()

    pg.hotkey("f11")
    pg.hotkey("ctrl", "w")
    messagebox.showinfo("AVISO", "Automação do Instagram, encerrada!")

main_bot()