from selenium import webdriver
from selenium.webdriver.common.by import By

import time
def obterDados(url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.get(url)

    driver.find_element(By.CSS_SELECTOR,"a.close-hit").click()

    
    nomereceita = driver.find_element(By.CLASS_NAME,"u-title-page")
    arquivo = open(f"{nomereceita.text}.txt","w")
    arquivo.write("NOME RECEITA: ")

    arquivo.write(f"{nomereceita.text} \n")

    arquivo.write("INGREDIENTES: \n")
    ingredientes = driver.find_elements(By.CLASS_NAME,"recipe-ingredients-item-label")

    for x in ingredientes:
        arquivo.write(f"- {x.text}\n")
        print(x.text)
    arquivo.write("PASSOS: \n")
    passos = driver.find_elements(By.CLASS_NAME,"recipe-steps-text")

    for x in range(len(passos)):
        arquivo.write(f"{x+1}- {passos[x].text}\n")
        print(passos[x].text)
    arquivo.write("CATEGORIAS: \n")
    categorias = driver.find_elements(By.CSS_SELECTOR,"a.button.button-tictac.button-tictac-grey")
    for x in categorias:
        arquivo.write(f"- {x.text}\n")
        print(x.text)
    driver.quit()
    



receitas = ["https://www.tudogostoso.com.br/receita/147817-file-de-peixe-ao-leite-de-coco.html","https://www.tudogostoso.com.br/receita/305306-ovo-recheado-com-torta-de-limao.html"]
for r in receitas:
    obterDados(r)

