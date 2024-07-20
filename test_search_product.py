from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_setup import setup_driver

def test_search_product(product_name):
    driver = setup_driver()
    driver.get("https://www.magazineluiza.com.br/")
    
    search_box = driver.find_element(By.ID, "input-search")
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)
    
    # Esperar até que a URL mude para a página de resultados
    WebDriverWait(driver, 10).until(
        EC.url_contains("busca")
    )
    
    # Esperar até que os elementos dos produtos estejam visíveis
    try:
        results = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='product-card-container']"))
        )
    except:
        results = []

    assert len(results) > 0, "Produtos não encontrados!"
    
    current_url = driver.current_url
    print(f"Encontrado {len(results)} produtos no link: {current_url}.")
    driver.quit()

def test_load(product_names):
    for product in product_names:
        print(f"Buscando produtos para: {product}")
        test_search_product(product)

if __name__ == "__main__":
    product_names = [
        "smartphone",
        "notebook",
        "television",
        "air fryer",
        "headphones"
    ]
    test_load(product_names)