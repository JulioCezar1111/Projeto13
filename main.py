# Instalar Bibliotecas: pyautogui (controla o mouse, tela e teclado)
#comando pyautogui.KEYBOARD_KEYS para ver todas as escritas do seu teclado
''''Automatização  anotar passo a passo:'''

#Biblioteca:
import pyautogui
import time

pyautogui.alert('O codigo vai começar não use o computador') #Imprimi uma messagem na tela
pyautogui.PAUSE = 2 # Ele aguarda 500 ms para execultado os comandos

#1º abrir o google drive no meu computador
pyautogui.press('winleft') #Metodod serve para apertar uma tecla do seu teclado
pyautogui.write('chorme') #Metodo para escrever
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')


#2º entrar na minha area de trabalho
pyautogui.hotkey('winleft', 'd') #Metodo para combinação de teclas (tecla de atalho)

'''posicao_mouse = pyautogui.position() #Da as coordenadas do mouse na tela
print(posicao_mouse)'''


#3º cliquei no arquivo que eu quero fazer backup e arrastei ele
pyautogui.moveTo(109, 550) #Metodo para mover o mouse
pyautogui.mouseDown() #Pressiona o botão do mouse por padrao ele pressiona o botão esquerdo do mouse
pyautogui.moveTo(-300, 513)

#4º enquanto eu estou arrastando, eu vou mudar para o google drivechorme
pyautogui.hotkey('alt', 'tab')


#5º larguei o arquivo no google drive
pyautogui.mouseUp() #Metodo solta o arquivo que estava sendo pressionado

#6º esperar 5 segundos
time.sleep(5)
pyautogui.alert('O codigo terminou pode usar o computador')