from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import datetime
import time
import random
import re

def tempo(segundos):
    return time.sleep(segundos)

h = input('Qual o horario de pesquisa? ')
n_pesquisas = int(input('Quantas pesquisas? '))

palavras_tratadas =[
    ['banana','caneta','dezena','farofa','hora','lixo','mamão','noite','pirulito','xícara','azedo','beijo','coleira','dúzia','goiaba','humano','jabuti','novela','oito','roupa','sabão','zero','tucano','xarope'],
    ['quiabo','barriga','pássaro','tesoura','chapéu','rainha','agulha','tartaruga','fósforo','feliz','globo','volante','pincel','livro','flor','cenoura','umbigo','colégio','guerra','creme','vidro','grama','planeta','bloco','clínica'],
    ['cabeleireiro','advogado','absurdo','desenhar','família','ontem','jeito','mexer','problema','preguiça','faxina','fugir','corrigir','jejum','micróbio','atraso','bicicleta','folclore','exemplo','atrás','mendigo','mortadela','bege','fogueira','caranguejo'],
    ['enxergar','sobrancelha','milionário','travesseiro','padrasto','madrasta','higiene','cadarço','quiseram','pesquisa','textual','quase','companhia','cérebro','refrigerante','prezado','periquito','asterisco','aptidão','hélice','coceira','pressa','explodir','ninguém'],
    ['bicarbonato','delinquente','perturbar','expansão','torácico','sessenta','meteorologia','privilégio','cônjuge','promessa','ziquizira','piscina','macete','empecilho','mal-humorado','exclamar','ansioso','confessar','necessidade','profissão','ziguezague','remessa','surpresa','idolatrado','cinquenta'],
    ['aquiescer','reivindicar','recauchutar','impressão','licença','estender','hesitar','supérfluo','coincidência','frustração','prostração','insensível','irrequieto','discussão','execução','consenso','distorção','procrastinar','prestígio','suspense','subsídio','experiência','caatinga','retrógrado','estéril'],
    ['vicissitude','concessão','maciço','exceção','ascensão','exórdio','beneficência','conspurcar','excesso','persistência','quinquilharia','obsessão','capcioso','coalizão','extraterrestre','infeccioso','exclusividade','abstinência','itinerância','incontrovérsia','impronunciamento','interdisciplinaridade','profissionalização','inconstitucional'],
    ['cóccix','consociação','idiossincrasia','assertividade','impeachment','réveillon','zooplâncton','inconsistência','percuciência','senescência','assoreamento','ressurreição','ascensorista','imunodeficiência','fosforescência','transubstanciação','meningocócito','antropocentrismo','incompatilibização','otorrinolaringologista','anticonstitucionalmente','desincompatibilização','incompreensibilidade','inconstitucionalissimamente','esternocleidomastoideo'],
] 


i = 1
while True:
    tme = datetime.datetime.now()
    hora = tme.strftime('%H')
    minuto = tme.strftime('%M')
    segundo = tme.strftime('%S')
    print(f'{hora}:{minuto}:{segundo}')
    tempo(1)
    if hora == h and minuto == '38':
        print('Acessou a condição')
        arquivo = open('Python/arq_test.txt', 'a')
        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        navegador.maximize_window()
        while i < n_pesquisas:
            a1 = random.randrange(1,7)
            a2 = random.randrange(0, len(palavras_tratadas[a1]))
            arquivo.write(f'Na {i} vez, ficou na pagina por {a1}s e pesquisou pela palavra {palavras_tratadas[a1][a2]}\n')
            navegador.get("https://www.google.com/")
            tempo(1)
            navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(palavras_tratadas[a1][a2])
            tempo(1)
            navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
            #navegador.get_screenshot_as_file(f'C:\prints\Print{i}.png')
            time.sleep(a1)
            i += 1
        navegador.quit()
        arquivo.close()



