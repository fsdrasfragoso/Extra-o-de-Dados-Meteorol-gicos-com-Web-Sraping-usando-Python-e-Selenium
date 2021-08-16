# importar as bibliotecas
from selenium import webdriver
import time
import MySQLdb
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://cartolafc.globo.com')
time.sleep(30)
driver.get('https://cartolafc.globo.com/#!/time/11137421')
time.sleep(5)
print("espera")
parcial = driver.find_element_by_xpath('//div[contains(@class,"cartola-time-adv__pontuacao pont-positiva")]').text
print(parcial)

    
    
