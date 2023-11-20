##### ================== Section for library import start ==================
import random
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import string
import requests
from fp.fp import FreeProxy
##### ================== Section for library import end ==================



##### ================== Section for lists start ==================
def make_request_with_proxy(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=5)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        return None

# Paid Proxies.txt file
proxies_file_path_paid = os.path.join("DATA", "Proxies_Paid.txt")
with open(proxies_file_path_paid, "r") as file:
    paid_proxies_list = [line.strip() for line in file]

# Free Proxies.txt file
proxies_file_path_free = os.path.join("DATA", "Proxies_Free.txt")
with open(proxies_file_path_free, "r") as file:
    free_proxies_list = [line.strip() for line in file]

# Attempt using FreeProxy library for the first 100 requests
for attempt in range(10):
    try:
        proxy = FreeProxy(country_id=['US', 'BR', 'CA']).get()
        print(f"Attempt {attempt + 1}: Using FreeProxy library. Proxy: {proxy}")
        response = make_request_with_proxy('https://www.google.com', proxy)
        if response:
            print(f"Request successful. Status Code: {response.status_code}")
            break
    except Exception as e:
        print(f"Error during attempt {attempt + 1} with FreeProxy library: {str(e)}")

        if attempt == 9:
            # All attempts with FreeProxy failed, try random proxy from Proxies_Free.txt 100 times
            for _ in range(10):
                random_proxy_free = "http://" + random.choice(free_proxies_list)
                print(f"Attempt {_ + 1}: Using random proxy from Proxies_Free.txt. Proxy: {random_proxy_free}")
                response = make_request_with_proxy('https://www.google.com', random_proxy_free)
                if response:
                    print(f"Request successful. Status Code: {response.status_code}")
                    break
            else:
                print("All attempts with Proxies_Free.txt failed.")

                # All attempts with Proxies_Free.txt failed, try random proxy from Proxies_Paid.txt
                for _ in range(10):
                    random_proxy_paid = "http://" + random.choice(paid_proxies_list)
                    print(f"Attempt {_ + 1}: Using random proxy from Proxies_Paid.txt. Proxy: {random_proxy_paid}")
                    response = make_request_with_proxy('https://www.google.com', random_proxy_paid)
                    if response:
                        print(f"Request successful. Status Code: {response.status_code}")
                        break
                else:
                    print("All attempts with Proxies_Paid.txt failed.")
# Headers.txt file
headers_file_path = os.path.join("DATA", "Headers.txt")
with open(headers_file_path, "r") as file:
    user_agents = [line.strip() for line in file]
random_user_agent = random.choice(user_agents)
print(random_user_agent)
# Elements.txt file
elements_file_path = os.path.join("DATA", "Elements.txt")
with open(elements_file_path, "r") as file:
    elements_data = [line.strip() for line in file]
# First_Name.txt file
first_name_file_path = os.path.join("DATA", "First_Name.txt")
with open(first_name_file_path, "r") as file:
    first_names = [line.strip() for line in file]
random_first_name = random.choice(first_names)
print(random_first_name)
# SurName.txt file
Surname_file_path = os.path.join("DATA", "SurName.txt")
with open(Surname_file_path, "r") as file:
    Surnames = [line.strip() for line in file]
random_surname = random.choice(Surnames)
print(random_surname)
##### ================== Section for lists end ==================

##### ================== Section for random list generation start ==================
# Time delay setup
x = 5
y = 11
random_wait_time = random.uniform(x, y)
# Generate random birthday details (J=Jan, F=Feb, M=March, A=April, S=Sept, O=Oct, N=Nov, D=Dec)
Birthday_Day = str(random.randint(1, 28))
print(Birthday_Day)
Birthday_Year = str(random.randint(1945, 2004))
print(Birthday_Year)
month_initials = ['J', 'F', 'M', 'A', 'S', 'O', 'N', 'D']
random_month_initial = random.choice(month_initials)
print(random_month_initial)
# Choose random gender (M=Male, F=Female, R=Rather Not Say)
Gender_initials = ['M', 'F', 'R']
random_Gender_initial = random.choice(Gender_initials)
print(random_Gender_initial)
# Generate random username for custom email address
rand_5_digit_num = str(random.randint(0, 999999))
special_char = list(string.ascii_lowercase)
random_special_char = random.choice(special_char)
user_name = random_first_name + random_special_char + random_surname
user_name = user_name.lower() + random_special_char + str(rand_5_digit_num)
print(user_name)
# Generates random password 8-16 characters long
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
size = random.randint(8, 18)
password = ''.join(random.choice(chars) for _ in range(size))
print(password)
##### ================== Section for random list generation end ==================

##### ================== Section for generate phone number start ==================
API_KEY = ""
Country_Codes = [12, 36]  #12 = US, 36 = Canada
COUNTRY_CODE = random.choice(Country_Codes) 
sms_activate_url = "https://sms-activate.org/stubs/handler_api.php"
phone_request_params = {
    "api_key":API_KEY,
    "action":"getNumber",
    "country":COUNTRY_CODE, 
    "service":"go",
}
status_param = {
    "api_key":API_KEY,
    "action":"getStatus"
}
number = ""
activationId = ""
while True:
    res = requests.get(url=sms_activate_url, params=phone_request_params)
    data = res.text
    if "ACCESS_NUMBER" in data:
        activationId = data.split(':')[1]
        number = data.split(':')[2]
        number = '+' + number
        print(number)
        break
##### ================== Section for generate phone number end ==================


# Extract the elements into separate lists
Create_Account_Element = []
For_My_Personal_Use_Element = []
First_Name_Element = []  
Surname_Element = []
Birthday_Day_Element = []
Birthday_Month_Element = []
Birthday_Year_Element = []
Gender_Element = []
Next_Element = []
Username_Select_Element = []
Username_Element = []
Password_Element = []
Confirm_Password_Element = []
Phone_Number_Element = []
OTP_Element = []

# Tracks the current list
element_list = None  
for line in elements_data:
    if line.startswith("For_My_Personal_Use_Element"):
        element_list = For_My_Personal_Use_Element
    elif line.startswith("Create_Account_Element"):
        element_list = Create_Account_Element
    elif line.startswith("First_Name_Element"):
        element_list = First_Name_Element
    elif line.startswith("Surname_Element"):
        element_list = Surname_Element
    elif line.startswith("Birthday_Day_Element"):
        element_list = Birthday_Day_Element        
    elif line.startswith("Birthday_Month_Element"):
        element_list = Birthday_Month_Element        
    elif line.startswith("Birthday_Year_Element"):
        element_list = Birthday_Year_Element
    elif line.startswith("Gender_Element"):
        element_list = Gender_Element
    elif line.startswith("Next_Element"):
        element_list = Next_Element
    elif line.startswith("Username_Select_Element"):
        element_list = Username_Select_Element
    elif line.startswith("Username_Element"):
        element_list = Username_Element
    elif line.startswith("Password_Element"):
        element_list = Password_Element    
    elif line.startswith("Confirm_Password_Element"):
        element_list = Confirm_Password_Element
    elif line.startswith("Phone_Number_Element"):
        element_list = Phone_Number_Element
    elif line.startswith("OTP_Element"):
        element_list = OTP_Element
    elif element_list is not None:
        element_list.append(line)

URL = "https://accounts.google.com"

chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_argument(f'user-agent={random_user_agent}')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument(f'--proxy-server={proxy}')
driver = webdriver.Chrome(options=chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => false})")
driver.get(URL)
time.sleep(random.uniform(15, 45))

for xpath in Create_Account_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in For_My_Personal_Use_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(10)

for xpath in First_Name_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(random_first_name)
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Surname_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(random_surname)
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Next_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Birthday_Day_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(Birthday_Day)
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Birthday_Month_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(random_month_initial)
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Birthday_Year_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(Birthday_Year)
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Gender_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(random_Gender_initial)
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Next_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Username_Select_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Username_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(user_name)
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Next_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Password_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(password)
        break
    except:
        pass
time.sleep(random_wait_time)
      
for xpath in Confirm_Password_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(password)
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Next_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Phone_Number_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(number)
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Next_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

code = ''
while True:
    status_param['id'] = activationId
    print(status_param)
    res_code = requests.get(url=sms_activate_url, params=status_param)
    data_code = res_code.text
    print(data_code)
    if "STATUS_OK" in data_code:
        code = data_code.split(':')[1]
        break
time.sleep(15)  

for xpath in OTP_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(code)
        break
    except:
        pass
time.sleep(random_wait_time)

for xpath in Next_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

#   BREAKS HERE DOES NOT CHOOSE SKIP, AFTER THIS NOT TESTED
#SKIP
for xpath in Next_Element: # may have to change this to a new skip element on its own as may be conflicting with the next element as both on same page
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

#SKIP
for xpath in Next_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

#NEXT
for xpath in Next_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

#SCROLL TO CHECK
driver.execute_script("window.scrollTo(0, 800)")
time.sleep(random_wait_time)

#I AGREE
for xpath in Next_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)

#CONFIRM
for xpath in Next_Element:
    try:
        element = WebDriverWait(driver, random_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()
        break
    except:
        pass
time.sleep(random_wait_time)


month_mapping = {
    'J': 'January',
    'F': 'February',
    'M': 'March',
    'A': 'April',
    'S': 'September',
    'O': 'October',
    'N': 'November',
    'D': 'December',
}

# Convert random_month_initial to the corresponding month name
month_name = month_mapping.get(random_month_initial, 'Unknown')
birthday = Birthday_Day + "/" + month_name + "/" + Birthday_Year
# Save information to CSV
csv_file = 'OUTPUT.csv'
output_data = [random_first_name, random_surname, birthday, user_name, password, number]

# Check if the file exists and write header only if it's a new file
write_header = not os.path.exists(csv_file)

with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)

    # Write header only if the file is new
    if write_header:
        writer.writerow(['First Name', 'Surname', 'Birthday', 'Username', 'Password', 'Number'])

    # Write the data to the CSV file
    writer.writerow(output_data)

# Wait for 2 minutes (120 seconds) before closing the browser
time.sleep(120)

# Close the driver when you're done
driver.quit()

