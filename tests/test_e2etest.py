
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    # Hacer clic en el enlace de la tienda
    driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    # Obtener todos los productos
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    def addProductToCart(productToAdd, products):
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == productToAdd:
                product.find_element(By.XPATH, "div/button").click()
                break

    # Usar la función para agregar producto al carrito
    addProductToCart("Samsung Note 8", products)

    # Ir al carrito
    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

    # Proceder al checkout
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    # Ingresar país
    driver.find_element(By.ID, "country").send_keys("spa")

    # Esperar y seleccionar España
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Spain")))
    driver.find_element(By.LINK_TEXT, "Spain").click()

    # Marcar checkbox y realizar compra
    driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
    driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()

    # Verificar mensaje de éxito
    alertsuccess = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success!" in alertsuccess
