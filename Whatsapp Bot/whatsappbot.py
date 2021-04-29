from selenium import webdriver 
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#navegar até o Whatsapp Web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
#defiinir contatos e grupos e mensagem a ser enviada
contatos = ['grupo pra texto', 'Grupo 4 - Rial pizzas']
mensagem = 'ola eai beleza isso é um teste'
# buscar contatos /grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

    