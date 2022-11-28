
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class DemoExplicitWait():
    def exp_wait(self):
        browser = webdriver.Chrome(service=Service
                                   (executable_path=ChromeDriverManager().install()))
        wait = WebDriverWait(browser, 10)
        browser.get("https://www.yatra.com")
        # browser.find_element(
        #     By.XPATH, "//input[@id='BE_flight_origin_city']").click()
        browser.maximize_window()
        # deprt = wait.until(EC.invisibility_of_element_located(
        # (By.XPATH, "//input[@id='BE_flight_origin_city']")))
        deprt = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        # time.sleep(4)
        # deprt = browser.find_element(
        #     By.XPATH, "//input[@id='BE_flight_origin_city']")
        deprt.click()
        # act = ActionChains(browser)
        # act.double_click(deprt).perform()
        time.sleep(2)
        deprt.send_keys("New Delhi")
        time.sleep(2)
        deprt.send_keys(Keys.ENTER)

        arrival = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        arrival.click()
        time.sleep(2)
        arrival.send_keys("New York")
        cntrylst = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='viewport']//div[1]/li")))
        print(len(cntrylst))
        for cntry in cntrylst:
            print(cntry.text)
            if "New York(JFK)" in cntry.text:
                cntry.click()
                break

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        # origin = browser.find_element(
        #     By.XPATH, "//input[@id='BE_flight_origin_date']")
        # origin.click()
        # time.sleep(6)
        # browser.find_element(
        #     By.CSS_SELECTOR, "input[title= \'Tuesday, 5 July 2022\'").click()
        # time.sleep(4)

        all_dates = wait.until(EC.element_to_be_clickable
                               ((By.XPATH, "//div[@id='month-wrapper']//tbody//td[@class!='inActiveTD']"))).find_elements(By.XPATH, "//div[@id='month-wrapper']//tbody//td[@class!='inActiveTD']")
        # [dt.click()
        #  for dt in all_dates if dt.get_attribute("data-date") == "04/07/2022"]
        for dt in all_dates:
            if dt.get_attribute("data-date") == "04/07/2022":
                dt.click()
                break
        browser.find_element(
            By.XPATH, "//input[@value='Search Flights']").click()


dauto = DemoExplicitWait
dauto.exp_wait()
