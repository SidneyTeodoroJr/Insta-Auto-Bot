<h1 align="center">Insta Auto Bot</h1>
</br>

<div align="center">
<img src="https://github.com/SidneyTeodoroJr/instagram_like_robot/blob/main/img/Instagram%20Like%20Bot.jpg" alt="Digital Whiteboard">
</div>
</br>
</br>


## Visão Geral
<p>
 Este é um projeto de automação para interagir com o Instagram, para automatizar a interação com publicações, dando "likes" em postagens. O bot utiliza a biblioteca PyAutoGUI para simular a navegação humana.
<p/>

<video id="VisaChipCardVideo" width="1080" controls>
 <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
</video>

### Tecnologias usada:
[Python](https://docs.python.org/3/)<br/>
﻿[OS](https://docs.python.org/3/library/os.html)<br/>
[Time](https://docs.python.org/3/library/time.html)<br/>
[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)<br/>
[webbrowser](https://docs.python.org/3/library/webbrowser.html)<br/>
[pynput](https://pypi.org/project/pynput/)<br/>
[tkinter](https://docs.python.org/pt-br/3/library/tkinter.html)<br/>
[opencv](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)<br/>
[PyScreeze](https://pypi.org/project/PyScreeze/)<br/>

## Estrutura do Projeto
<p>
O projeto está dividido para melhor organização e modularidade.
<p/>
<br/>

1. [main.py](https://github.com/SidneyTeodoroJr/Bolsa_de_Valores/blob/main/src/main.py): O ponto de entrada da aplicação que importa e utiliza os módulos e scripts necessários.
2. [page.py](https://github.com/SidneyTeodoroJr/Bolsa_de_Valores/blob/main/src/modulos/page.py):  localizar uma imagem específica na tela e interagem automaticamente.<br/><br/>

## Funcionalidades   

. Abre o navegador e acessa o Instagram.<br/>
. Localiza e clica em botões de "like" nas postagens.<br/>
. Detecta a tecla 'ESC' para interromper a automação.<br/>

## Instruções de Execução
1. ative o ambiente virtual:
   ```shell
   bot/Scripts/Activate.ps1 
2. Instale as dependências necessárias usando:
    ```shell
    pip install -r requirements.txt
3. Execute o o bot com o comando:
   ```shell
   python src\main.py
4. Acesse a aplicação no navegador.

## Customização

. Você pode ajustar o `tempo` de espera e a `confidence` na correspondência da imagem na classe `ImageLocator` para melhorar a precisão da automação. <br/><br/>
. Adicione ou remova imagens na lista da função `bot_click_like()` para personalizar as ações do bot. <br/><br/>

## Aviso

<p>
  Este projeto é apenas para fins educacionais. O uso indevido deste bot pode violar os termos de serviço do Instagram e resultar na suspensão da sua conta. Use por sua conta e risco.
<p/>

 ## Contribuições
</br>

<p>
Contribuições são bem-vindas! Se quiser melhorar o projeto, adicionar novas funcionalidades ou corrigir problemas, fique à vontade.
</p>
<hr>
</br>

<div align="center">
<a href="https://sidney-personal-portifolio.netlify.app/"><img src="https://img.shields.io/badge/-Portifolio-%230077B5?style=for-the-badge&logo=portifolio&logoColor=white" style="border-radius: 30px" target="_blank" /></a>
<a href="https://www.instagram.com/sidneyteodoroaraujo" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
<a href="https://www.linkedin.com/in/sidney-teodoro-4a4a8119b?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B%2FevuTOiSSJS2hWGCZgtZiQ%3D%3D" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px" target="_blank" /></a>
</div>

 
