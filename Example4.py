from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import traceback

# Read data from JSON file
with open('C:/Users/a.islam/OneDrive - Reply/Documents/Testing Docs/Automation/SUPERVISOR_NO_FLAG.json', 'r') as file:
    data = json.load(file)
print(data)

# Create a Firefox WebDriver instance
firefox_driver = webdriver.Firefox()
firefox_driver.maximize_window()

try:
    # Open the Siebel web application URL
    firefox_driver.get('https://10.64.125.34:8002/siebel/app/admin/enu?SWECmd=GotoView&SWEView=Organizations&SWERF=1&SWEHo=&SWEBU=1&SWEApplet0=Organization+List+Applet&SWERowId0=1-1PCWCGX')

    # Assuming you need to log in - replace these steps with your actual login process
    username_input = firefox_driver.find_element('id', 's_swepi_1')
    password_input = firefox_driver.find_element('id', 's_swepi_2')

    username_input.send_keys('Cheetah20')
    password_input.send_keys('CHEETAH2020!4')
    login_button = firefox_driver.find_element('id', 's_swepi_22')
    login_button.click()

    # Wait for the Search box to be clickable
    search = WebDriverWait(firefox_driver, 90).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-labelledby="QueryComboBox_Label_2"]')))
    
    # Scroll the element into view using JavaScript
    #firefox_driver.execute_script("arguments[0].scrollIntoView(true);", search)
    ActionChains(firefox_driver).move_to_element(search).perform()

    # Clear any existing value in the textbox
    search.clear()

    # Write a value into the textbox
    search.send_keys('Name')
    print("Successfully put value 'Name' on the field")
    search.send_keys(Keys.RETURN)
    print("Successfully press enter on the search field")

    for item in data:
        # Extract the values for each item
        user_id_value = item['EMPLOYEE']
        provider_name_value = item['PROVIDER']
    
    # Wait for the provider name input box to be clickable
        provider_name = WebDriverWait(firefox_driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @name='s_2_1_12_0' and @aria-labelledby='QuerySrchSpec_Label_2']")))
        ActionChains(firefox_driver).move_to_element(provider_name).perform()
    
    # Clear any existing value in the textbox
        provider_name.clear()   
    # Write a value into the textbox
        provider_name.send_keys(provider_name_value)
        print("Successfully entered value into the provider name box")
        provider_name.send_keys(Keys.RETURN)
        print("Successfully press enter on the search field")


    # Wait for the supervisor input box to be clickable
        supervisor = WebDriverWait(firefox_driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s_1_1_19_0_icon"]')))
        ActionChains(firefox_driver).move_to_element(supervisor).perform()
    
    # Click on the supervisor input box to open the pop-up window
        supervisor.click()
        print("Successfully clicked on the supervisor field")

    # Wait for the dialog window to appear (adjust timeout as needed)
        WebDriverWait(firefox_driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="s_1_1_19_0_icon"]')))


    # Now you can locate and interact with the elements inside the dialog window
        #search1 = WebDriverWait(firefox_driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="text" and @name="s_4_1_42_0" and @aria-labelledby="PopupQueryCombobox_Label_4" and @aria-label="Find" and contains(@class,"siebui-ctrl-select siebui-input-popup siebui-align-left siebui-input-align-left ui-autocomplete-input") and @title="Find"]')))
        search1 = WebDriverWait(firefox_driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="text" and contains(@name, "s_") and contains(@name, "_42_0")]')))
    # Clear any existing value in the textbox
        search1.clear()
        search1.send_keys('Login')
        search1.send_keys(Keys.RETURN)
        print("Successfully entered Login")


    # Now you can locate and interact with the elements inside the dialog window
        #search2 = WebDriverWait(firefox_driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="siebui-ctrl-input siebui-align-left siebui-input-align-left s_4_1_43_0" and @title="Starting with"]')))
        search2 = WebDriverWait(firefox_driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[starts-with(@name, "s_") and contains(@name, "_1_43_0")]')))
    # Clear any existing value in the textbox
    #search2.click()
        search2.send_keys(user_id_value)
        search2.send_keys(Keys.RETURN)
        print("Successfully entered UID")


    # Now you can locate and interact with the elements inside the dialog window
        #Row1 = WebDriverWait(firefox_driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="1_s_4_l_LH_Supervisor"]')))
        Row1 = WebDriverWait(firefox_driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "1_s_") and contains(@id, "_LH_Supervisor")]')))
    # Clear any existing value in the textbox
        Row1.click()
        print("Successfully click row 1")


        #checkbox = WebDriverWait(firefox_driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-labelledby="1_s_4_l_Login s_4_l_LH_Supervisor s_4_l_altCheckBox"]')))
        checkbox = WebDriverWait(firefox_driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="1_LH_Supervisor"][aria-labelledby*="_Login"]')))
        #ActionChains(firefox_driver).move_to_element(checkbox).perform()
        #checkbox.click()
        if not checkbox.is_selected():
            ActionChains(firefox_driver).move_to_element(checkbox).perform()
            checkbox.click()

        print("Successfully click checkbox")


        #save = WebDriverWait(firefox_driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="s_4_1_45_0_Ctrl"]')))
        save = WebDriverWait(firefox_driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "_1_45_0_Ctrl")]')))
        ActionChains(firefox_driver).move_to_element(save).perform()
        save.click()
    #if not checkbox.is_selected():
    # If not selected, click the checkbox to select it
        #checkbox.click()

        print("Successfully save it")

    
except TimeoutException:
    # Handle timeout exception if the element is not clickable within the specified time
    print("Timeout exception: The User tab is not clickable within the specified time")

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()

#finally:
    # Close the Firefox browser window
    #firefox_driver.quit()
