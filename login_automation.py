# Import the necessary Selenium modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# Set the path to your ChromeDriver executable
# Example paths for Windows and macOS/Linux:
# For Windows:
# chromedriver_path = 'chromedriver.exe'
# For macOS/Linux:
chromedriver_path = './chromedriver'

# Specify the ChromeDriver service
chrome_service = ChromeService(executable_path=chromedriver_path)

# Initialize the web driver using the ChromeDriver service
driver = webdriver.Chrome(service=chrome_service)

# Navigate to the web application login page
driver.get('https://www.example.com/login')  # Replace with the actual URL of your web application's login page

# Find the username and password input fields and the login button using their HTML attributes
username_input = driver.find_element(By.ID, 'username')  # Replace 'username' with the actual ID of the username input field
password_input = driver.find_element(By.ID, 'password')  # Replace 'password' with the actual ID of the password input field
login_button = driver.find_element(By.ID, 'login-button')  # Replace 'login-button' with the actual ID of the login button

# Enter the username and password
username_input.send_keys('your_username')  # Replace 'your_username' with your actual username
password_input.send_keys('your_password')  # Replace 'your_password' with your actual password

# Click the login button to submit the form
login_button.click()

# Wait for a few seconds to ensure the login process completes
driver.implicitly_wait(5)

# Check if the login was successful by verifying a specific element on the next page
if 'Dashboard' in driver.title:  # Replace 'Dashboard' with a unique title or element text on the page you land after successful login
    print('Login successful!')
else:
    print('Login failed.')

# Close the browser
driver.quit()
