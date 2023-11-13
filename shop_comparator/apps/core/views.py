from django.views import generic


class HomePage(generic.TemplateView):
    from selenium import webdriver
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from time import sleep

    driver = webdriver.Chrome()

    driver.get("https://www.sephora.fr/p/l-interdit---eau-de-parfum-rouge-562283.html")

    sleep(2)

    btn = driver.find_element(By.ID, "footer_tc_privacy_button_2").click()

    end_date_promo = driver.find_element(By.CSS_SELECTOR, 'div.text-flag-enddate').find_element(By.CSS_SELECTOR,
                                                                                                'span.text-flag-label')

    marque = driver.find_element(By.CLASS_NAME, "brand-name")

    product_name = driver.find_element(By.CLASS_NAME, "product-name")

    driver.quit()

    template_name = 'pages/index.html'
