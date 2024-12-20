from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import Keys to use it
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# Full path to the WebDriver executable
driver_path = "C:/Users/HP/OneDrive/Desktop/driver/chromedriver-win64/chromedriver.exe"  # Update this if needed
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")  # Replace with the actual URL

# Wait for the username field to be visible and interact with it
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
username_field.send_keys("Admin")  # Replace with the actual username
print("Entered the username successfully.")

# Wait for the password field to be visible and interact with it
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
password_field.send_keys("admin123")  # Replace with the actual password
print("Entered the password successfully.")

# Wait for the login button to be clickable and then click it
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))
    )
    driver.execute_script("arguments[0].click();", login_button)  # Click using JavaScript if standard click doesn't work
    print("Login button clicked successfully.")
except TimeoutException:
    print("Error: The login button is not clickable within the timeout period.")

# Wait for the page to load by checking for an element that exists only after login
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Dashboard')]")))
    print("Page loaded successfully.")
except TimeoutException:
    print("Error: The page did not load within the timeout period.")
    

# Wait for the PIM module to be clickable and then click it
try:
    pim_module = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-main-menu-item']/span[text()='PIM']"))
    )
    pim_module.click()  # Click the PIM module
    print("PIM module clicked successfully.")
except TimeoutException:
    print("Error: The PIM module is not clickable within the timeout period.")

# Wait for the PIM page to load by checking for an element that's only visible on the PIM page (e.g., an element specific to PIM)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Employee Information')]")))
    print("PIM page loaded successfully.")
except TimeoutException:
    print("Error: The PIM page did not load within the timeout period.")

# Scroll down by 500 pixels to the mid-level of the page
driver.execute_script("window.scrollBy(0, 500);")  # Scroll down by 500 pixels

# Wait for the Add button to be visible and clickable before clicking it
try:
    add_emp = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[.//i[contains(@class, 'oxd-icon') and contains(@class, 'bi-plus')]]"))
    )
    # Use JavaScript click if the standard click doesn't work
    driver.execute_script("arguments[0].click();", add_emp)
    print("Add button clicked successfully.")
except TimeoutException:
    print("Error: The Add button is not clickable within the timeout period.")

# Wait for an element specific to the Add Employee page to be visible, confirming that the page loaded
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h5[text()='Add Employee']"))  # Replace with a unique element that confirms Add Employee page
    )
    print("Add Employee page loaded successfully.")
except TimeoutException:
    print("Error: The Add Employee page did not load within the timeout period.")
    
# Wait for the First Name input field to be visible and interact with it
try:
    first_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='firstName']")))  # Unique XPath for First Name input field
    
    first_name_field.send_keys("James GTAS")  # Enter the first name
    print("First name entered successfully.")
except TimeoutException:
    print("Error: The First Name field is not visible or interactable within the timeout period.")

# Wait for the Middle Name input field to be visible and interact with it
try:
    middle_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='middleName']")))  # Unique XPath for Middle Name input field
    
    middle_name_field.send_keys("R")  # Enter the middle name
    print("Middle name entered successfully.")
except TimeoutException:
    print("Error: The Middle Name field is not visible or interactable within the timeout period.")

# Wait for the Last Name input field to be visible and interact with it
try:
    last_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='lastName']")))  # Unique XPath for Last Name input field
    
    last_name_field.send_keys("Tarvis Doubled")  # Enter the last name
    print("Last name entered successfully.")
except TimeoutException:
    print("Error: The Last Name field is not visible or interactable within the timeout period.")

# Wait for the toggle button to be visible and clickable
try:
    toggle_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-switch-input')]"))
    )
    toggle_button.click()  # Click to enable the toggle
    print("Toggle button enabled successfully.")
except TimeoutException:
    print("Error: Toggle button is not clickable within the timeout period.")

# Locate the input field using the unique XPath and enter the username
try:
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@class='oxd-input oxd-input--active' and @autocomplete='off']"))
    )
    username_field.send_keys("darvinsd@qw")  # Replace "YourUsername" with the actual username
    print("Username entered successfully.")
    
except Exception as e:
    print(f"Error: {e}")
# Locate the password input field using the unique XPath and enter the password
try:
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@class='oxd-input oxd-input--active' and @type='password' and @autocomplete='off']"))
    )
    password_field.send_keys("jarvis@74*")  # Replace "YourPassword" with the actual password
    print("Password entered successfully.")
except TimeoutException:
    print("Error: Password field is not visible or interactable within the timeout period.")
try:
    confirm_password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@class='oxd-input oxd-input--active' and @type='password' and @autocomplete='off']"))
    )
    confirm_password_field.send_keys("jarvis@74*")  # Replace with the actual confirm password
    print("Confirm password entered successfully.")
except TimeoutException:
    print("Error: Confirm Password field is not visible or interactable within the timeout period.")

# Use the unique XPath to locate and click the Save button
try:
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"))
    )
    save_button.click()
    print("Save button clicked successfully.")
except Exception as e:
    print(f"Error: {e}")

try:
    
    # Wait for the input box to be present
    wait = WebDriverWait(driver, 10)  # Adjust timeout as necessary
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input")))

    # Retrieve the value from the input field
    employee_id = input_box.get_attribute("value")

    # Print the Employee ID
    print(f"Employee ID: {employee_id}")

except Exception as e:
    print(f"Error occurred: {e}")

try:
    # Wait for the Employee List link to be present and click it
    wait = WebDriverWait(driver, 10)  # Adjust timeout as necessary
    employee_list_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Employee List']")))

    # Click the Employee List link
    employee_list_link.click()

    # Optionally, wait for the new page or action to complete
    time.sleep(2)

except Exception as e:
    print(f"Error occurred: {e}")

# Wait for the Employee Name input field to be visible and interact with it
try:
    # Adjust the XPath index to target the correct field
    employee_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Type for hints...'])[1]"))
    )
    
    # Enter the employee name
    employee_name_field.send_keys("James GTAS")
    print("Employee name entered successfully.")
except TimeoutException:
    print("Error: The Employee Name field is not visible or interactable within the timeout period.")

try:
    # Wait for the Search button to be clickable
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"))
    )
    # Click the Search button
    search_button.click()
    print("Search button clicked successfully.")
except TimeoutException:
    print("Error: Search button is not clickable within the timeout period.")

try:
    # Wait for the edit icon to be clickable
    edit_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']"))
    )
    # Click the edit icon
    edit_icon.click()
    print("Edit icon clicked successfully.")
except TimeoutException:
    print("Error: The edit icon is not clickable within the timeout period.")

try:
    # Wait for the specific radio button to be clickable (e.g., the second one)
    radio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[2]"))
    )
    # Click the radio button
    radio_button.click()
    print("Radio button clicked successfully.")
except TimeoutException:
    print("Error: The radio button is not clickable within the timeout period.")
try:
    # Wait for the Save button to be clickable
    save_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button)[1]"))
    )
    # Click the Save button
    save_button1.click()
    print("Save button clicked successfully.")
except TimeoutException:
    print("Error: The Save button is not clickable within the timeout period.")

try:
    # Wait for the Employee List link to be present and click it
    wait = WebDriverWait(driver, 10)  # Adjust timeout as necessary
    employee_list_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Employee List']")))

    # Click the Employee List link
    employee_list_link.click()

    # Optionally, wait for the new page or action to complete
    time.sleep(2)

except Exception as e:
    print(f"Error occurred: {e}")


try:
    # Adjust the XPath index to target the correct field
    employee_name_field1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Type for hints...'])[1]"))
    )
    
    # Enter the employee name
    employee_name_field1.send_keys("James GTAS")
    print("Employee name entered successfully.")
except TimeoutException:
    print("Error: The Employee Name field is not visible or interactable within the timeout period.")

try:
    # Wait for the Search button to be clickable
    search_buttons = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"))
    )
    # Click the Search button
    search_buttons.click()
    print("Search button clicked successfully.")
except TimeoutException:
    print("Error: Search button is not clickable within the timeout period.")
try:
    # Wait for the delete button to be clickable
    delete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-trash']"))
    )
    # Click the delete button
    delete_button.click()
    print("Delete button clicked successfully.")
except TimeoutException:
    print("Error: The delete button is not clickable within the timeout period.")

try:
    # Wait for the Yes, Delete button to be clickable
    delete_confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'))
    )
    # Click the Yes, Delete button
    delete_confirm_button.click()
    print("Delete confirmation clicked successfully.")
except TimeoutException:
    print("Error: The delete confirmation button is not clickable within the timeout period.")


print("Holding the screen for 1 minute. Do not close the browser manually.")
time.sleep(60)  # Wait for 60 seconds (1 minute)

# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")  # Replace with the actual URL

# Wait for the username field to be visible and interact with it
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
username_field.send_keys("Admin")  # Replace with the actual username
print("Entered the username successfully.")

# Wait for the password field to be visible and interact with it
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
password_field.send_keys("admin123456")  # Replace with the actual password
print("Entered the password successfully.")

# Wait for the login button to be clickable and then click it
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))
    )
    driver.execute_script("arguments[0].click();", login_button)  # Click using JavaScript if standard click doesn't work
    print("Login button clicked successfully.")
except TimeoutException:
    print("Error: The login button is not clickable within the timeout period.")