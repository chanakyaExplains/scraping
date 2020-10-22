from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import NoSuchElementException

print()
print("Slow internet may cause this program to crash.")
print()
adress = "none"
Country_names = []


def create_and_click(button, driver):
    click_it = ActionChains(driver)
    click_it.click(button)
    click_it.perform()


def format_output(text=" "):
    text = text.split("\n")
    print("Delevery   Cost       Carrier")
    for i in range(0, len(text)-1):
        if (i + 1) % 2 == 0:
            print(text[i] + "   " + text[i+1])


# while "https://www.aliexpress.com/item/" not in adress:
#     adress = input("Please enter your url : ")
#     if "https://www.aliexpress.com/item/" in adress:
#         break
#     print("Enter a proper aliexpress url please.")
#     print()

# adress = adress.strip('"')
#adress = "https://www.aliexpress.com/item/32607702449.html"
adress = "https://www.aliexpress.com/item/32552896653.html"

print()
print("This program will take a while to get all the values.")
print("You could minimize the program and let it run in the")
print("background and do something else.")
print()
print("Don't interact whith the web page as that will break the")
print("Action chain.")
print()

chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(adress)
sleep(12)

dilivery_button = driver.find_element_by_xpath(
    "/html/body/div[6]/div/div[2]/div/div[2]/div[10]/span[1]")

xpath1 = "/html/body/div[6]/div/div[2]/div/div[2]/div[10]/span[1]"
xpath2 = "/html/body/div[13]/div[2]/div/div[1]/div/div[2]/span"
xpath3 = "/html/body/div[13]/div[2]/div/div[1]/div/div[2]/span/div/div/div/span/span/span/span/input"

if dilivery_button.text == "Can not deliver ":
    xpath1 = "/html/body/div[6]/div/div[2]/div/div[2]/div[10]/span[2]"

dilivery_button = driver.find_element_by_xpath(xpath1)
create_and_click(dilivery_button, driver)
sleep(4)

country_select = driver.find_element_by_xpath(xpath2)
check_country = ActionChains(driver)
check_country.click(country_select)
check_country.perform()

list_of_countries = driver.find_elements_by_class_name("next-menu-item")

for i in range(6, len(list_of_countries)-1):
    Country_names.append(list_of_countries[i].text)

country_search = driver.find_element_by_xpath(xpath3)

print()
for country in Country_names:
    country_search.send_keys(country)
    sleep(2)
    country_to_click = driver.find_element_by_xpath(
        "/html/body/div[13]/div[2]/div/div[1]/div/div[2]/span/div/div/div/ul/li/div")
    create_and_click(country_to_click, driver)
    sleep(2)
    table = driver.find_element_by_xpath(
        "/html/body/div[13]/div[2]/div/div[1]/div/div[4]/div")
    print()
    print(country)
    print()
    format_output(table.text)
    print()
    sleep(1)
    check_country.perform()
    sleep(2)
sleep(2)
driver.quit()
