import os
import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
import datetime

def tempo(segundos):
    return time.sleep(segundos)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')
edge_service = Service(edge_driver_path)
edge_options = Options()
edge_options.add_argument(f'user-agent={user_agent}')
h = input('Qual o horario de pesquisa? ')
n_pesquisas = int(input('Quantas pesquisas? '))
i = 1

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

while True:
    tme = datetime.datetime.now()
    hora = tme.strftime('%H')
    minuto = tme.strftime('%M')
    segundo = tme.strftime('%S')
    print(f'{hora}:{minuto}:{segundo}')
    tempo(1)
    if hora == h and minuto == '07' and segundo == '00':
        print('Acessou a condição')
        arquivo = open('automacao_pesquisa/arq_test.txt', 'a')
        arquivo.write(f'Às {hora}horas, o programa iniciou as pesquisas\n')
        browser = webdriver.Edge(service=edge_service, options=edge_options)
        tempo(1)
        while i < n_pesquisas:
            a1 = random.randrange(1, 7)
            a2 = random.randrange(0, len(palavras_tratadas[a1]))
            arquivo.write(f'Na {i} vez, ficou na pagina por {a1}s e pesquisou pela palavra {palavras_tratadas[a1][a2]}\n')            
            browser.get(f'https://www.bing.com/search?q={palavras_tratadas[a1][a2]}&form=QBLH&sp=-1&ghc=1&pq=caca&sc=10-4&qs=n&sk=&cvid=FA483E9165524ABCBF35AA8FAE7B0AFF&ghsh=0&ghacc=0&ghpl=')
            tempo(a1)
            i += 1
        browser.quit()
        arquivo.close()