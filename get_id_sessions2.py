from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta



# Definindo a data inicial
data_inicial = datetime(2018, 3, 1)


# Obtendo a data de hoje
#data_atual = datetime.now()
data_atual = datetime(2018, 8, 1)



options = Options()
options.add_experimental_option("debuggerAddress", "localhost:8989")

# Make sure to provide the correct path to chromedriver.exe
chrome_driver_path = r'C:\Users\samsung\Desktop\driver\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Initialize the Chrome webdriver with the options
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get('https://www.esocial.gov.br/portal/Home/Inicial?tipoEmpregador=EMPREGADOR_GERAL')
#wait = WebDriverWait(driver, 5)
#button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="br-button sign-in large"]')))
#element = driver.find_element_by_xpath('//a[@href="/portal/download/Pedido/Consulta"]')
#button.click()
#element.click()
#https://login.esocial.gov.br/login.aspx


menu_download = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="menuDownload"]')))

# Clique no menu "Download"
menu_download.click()

# Aguarde até que o link "Consulta" seja clicável
link_consulta = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/portal/download/Pedido/Solicitacao"]')))

# Clique no link "Consulta"
link_consulta.click()

select_element = driver.find_element_by_id('TipoPedido')

# Use o método Select para interagir com o elemento
select = Select(select_element)

# Selecione a opção desejada pelo valor do atributo "value"
select.select_by_value('1')

# Localize o elemento de entrada de data pelo ID
data_element = driver.find_element_by_id('DataInicial')
data_element.clear()
data_element1 = driver.find_element_by_id('DataFinal')
data_element1.clear()


nova_data = "03/02/2023"  # Substitua esta string pela data que você deseja inserir
nova_data2 = "04/02/2023"
data_element.send_keys(nova_data)

# Pressione a tecla Enter para confirmar a entrada (opcional)
#data_element.send_keys(Keys.ENTER)


data_element1.send_keys(nova_data2)
#data_element1.send_keys(Keys.ENTER)

# Aguarde até que o botão "Salvar" seja clicável
botao_salvar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btnSalvar')))

# Clique no botão "Salvar"
botao_salvar.click()

menu_download = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="menuDownload"]')))

# Clique no menu "Download"
menu_download.click()

# Aguarde até que o link "Consulta" seja clicável
link_consulta = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/portal/download/Pedido/Solicitacao"]')))

# Clique no link "Consulta"
link_consulta.click()
