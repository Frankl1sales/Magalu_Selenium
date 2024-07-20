from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_setup import setup_driver
import time

def test_login():
    driver = setup_driver()
    driver.get("https://www.magazineluiza.com.br/")
    
    # Aguardar o botão de login estar presente e clicar nele
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.sc-iMTnTL.jTfMDA"))
        )
        print("Botão de login encontrado e clicado.")
        login_button.click()
    except Exception as e:
        print(f"Erro ao clicar no botão de login: {e}")
        driver.quit()
        return
    
    # Aguardar a página de login carregar completamente
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='login']"))
        )
    
    except Exception as e:
        print(f"Erro ao encontrar os campos de entrada: {e}")
        driver.quit()
        return
    
    assert email_input is not None, "Campo de email não encontrado!"
    
    print("Página de login carregada com sucesso.")
    time.sleep(10)
    # Preencher os campos de login e senha
    email_input.send_keys("franklinsales1711@gmail.com")  # Substitua pelo seu email
    
    # Clicar no botão "Continuar"
    try:
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.LoginBox-form-continue"))
        )
        continue_button.click()
        print("Botão 'Criar minha conta'.")
        # Esperar um pouco após clicar em "Continuar"
        time.sleep(20)  # Ajuste o tempo conforme necessário
    except Exception as e:
        print(f"Erro ao clicar no botão 'Criar minha conta': {e}")
    
    driver.quit()

if __name__ == "__main__":
    test_login()
