from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import re

arquivo = open("Python/banco_de_palavras.txt", "r")
navegador = webdriver.Edge(r'C:\\python\\msedgedriver.exe')
navegador.maximize_window()
palavras = arquivo.readlines()
palavras_tratadas = []
for i in palavras:
        y = re.sub(';\n', '', i)
        palavras_tratadas.append(y)
i = 1
while i < 3:    
    num_a = random.randrange(1,200)
    num_at = random.randrange(1,10)
   # print(f'Na {i} vez, ficou na pagina por {num_at}s e pesquisou pela palavra {palavras_tratadas[num_a]}')
    print('1')
    navegador.get('https://www.bing.com/')
    time.sleep(2)
    print('2')
    navegador.find_element('xpath','/html/body/div[1]/div/div[3]/main/form/div[1]/input').send_keys(palavras_tratadas[num_a])
    print('3')
    time.sleep(2)
    navegador.find_element('xpath','/html/body/div[1]/div/div[3]/main/form/div[1]/input').send_keys(Keys.ENTER)
    print('4')
    #navegador.get_screenshot_as_file(f'C:\prints\Print{i}.png')
    time.sleep(num_at)
    i += 1 

navegador.quit()
arquivo.close()