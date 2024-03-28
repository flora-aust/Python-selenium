from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import traceback

# Read data from JSON file
with open('C:/Users/a.islam/OneDrive - Reply/Documents/Testing Docs/Automation/SUPERVISOR_NO_FLAG.json', 'r') as file:
    data = json.load(file)

# Create a Firefox WebDriver instance
firefox_driver = webdriver.Firefox()

try:
    # Open the Siebel web application URL
    #firefox_driver.get('https://10.64.125.34:8002/siebel/app/admin/enu?SWECmd=Start')
    firefox_driver.get('https://10.64.125.34:8002/siebel/app/admin/enu?SWECmd=GotoView&SWEView=Organizations&SWERF=1&SWEHo=&SWEBU=1&SWEApplet0=Organization+List+Applet&SWERowId0=1-1PCWCGX')
    # Assuming you need to log in - replace these steps with your actual login process
    username_input = firefox_driver.find_element('id', 's_swepi_1')  # Replace with the actual element attributes
    password_input = firefox_driver.find_element('id', 's_swepi_2')

    username_input.send_keys('Cheetah20')
    password_input.send_keys('CHEETAH2020!4')
    login_button = firefox_driver.find_element('id', 's_swepi_22')
    login_button.click()

    #firefox_driver.refresh()
    # Wait for the Search box to be clickable
    search= WebDriverWait(firefox_driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="QueryComboBox_Label_2"]')))
    # Scroll the element into view
    firefox_driver.execute_script("arguments[0].scrollIntoView(true);", search)
    # Clear any existing value in the textbox (optional)
    search.clear()

    # Write a value into the textbox
    search.send_keys('Name')
    print("Successfully clicked on the name field")
    WebDriverWait(firefox_driver, 40).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @name='s_2_1_11_0' and @aria-labelledby='QueryComboBox_Label_2']"))) 


    #Wait for the Organizations link to be clickable
    provider_name= WebDriverWait(firefox_driver, 40).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @name='s_2_1_12_0' and @aria-labelledby='QuerySrchSpec_Label_2']")))
    # Scroll the element into view
    firefox_driver.execute_script("arguments[0].scrollIntoView(true);", provider_name)
    # Clear any existing value in the textbox (optional)
    provider_name.clear()
    # Write a value into the textbox
    provider_name.send_keys('LHinTouch')
    print("Successfully entered value into the provider name box")
    # Wait for the page to load after entering text into the provider_name_box
    WebDriverWait(firefox_driver, 40).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @name='s_2_1_12_0']"))) 

except TimeoutException:
    # Handle timeout exception if the element is not clickable within the specified time
    print("Timeout exception: The User tab is not clickable within the specified time")


        # Iterate over data and insert it into the application
    #for record in data:
            #employee_id = record.get('EMPLOYEE')
            #provider = record.get('PROVIDER')

            # Replace these steps with your actual logic to insert data
            #employee_id_input = firefox_driver.find_element('id', 'employee_id_input')
            #provider_input = firefox_driver.find_element('id', 'provider_input')

            #employee_id_input.send_keys(employee_id)
            #provider_input.send_keys(provider)
            # Add logic to submit the form or save the data
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()

finally:
    # Close the Firefox browser window
    firefox_driver.quit()
