from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from time import sleep
import yaml

with open('credentials.yml') as file:
    data = yaml.full_load(file)

# main variables
target_url = 'https://dopagent.indiapost.gov.in/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&__FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=3&BANK_ID=DOP&AGENT_FLAG=Y'
user_name = 'DOP.MI5600700400014'
password = 'ramurohan#105'

# page title
accounts_page_title = 'Department of Post Agent Login : Deposit Accounts'

# find by name 
name_username_entry = 'AuthenticationFG.USER_PRINCIPAL'
name_password_entry = 'AuthenticationFG.ACCESS_CODE'
name_login_button = 'Action.VALIDATE_RM_PLUS_CREDENTIALS_CATCHA_DISABLED'
name_accounts_href = 'HREF_Accounts'
name_agent_enquire_update_href = 'HREF_Agent Enquire & Update Screen'
name_go_to_page_button = 'Action.AgentRDActSummaryAllListing.GOTO_PAGE__'
name_fetch_more_accounts_button = 'Action.NEXT_ACCOUNTS'
name_page_number_entry = 'CustomAgentRDAccountFG.AgentRDActSummaryAllListing_REQUESTED_PAGE_NUMBER'
name_page_number_range = 'paginationtxt1'

# find by class
class_acount_details = 'searchsimpletext'

# find by xpath
xpath_account_number = "//a[@title='Hyperlink to view details of the account']"

def start_session():
    driver = webdriver.Firefox()
    return driver

def open_file(file_name, mode):
    fhand = open(file_name, mode)
    return fhand

def write_to_file(handle, string):
    handle.write(string)

def close_file(handle):
    handle.close()

def iterate_through_pages(driver, number_of_pages, file_handler):
    for i in range(1, number_of_pages+1):
        driver.find_element_by_name(name_page_number_entry).send_keys(str(i))
        driver.find_element_by_name(name_go_to_page_button).click()
        ac_details = driver.find_elements_by_class_name(class_acount_details)
        ac_numbers = driver.find_elements_by_xpath(xpath_account_number)
        to_print = ""
        for j in list(range(len(ac_details)))[0::4]:
            to_print += '{0: <8}'.format(str(i))
            to_print += '{0: <20}'.format(str(ac_numbers[(j//4)].text))
            to_print += '{0: <30}'.format(str(ac_details[j].text))
            to_print += '{0: <20}'.format(str(ac_details[j+1].text))
            to_print += '{0: <4}'.format(str(ac_details[j+2].text))
            to_print += str(ac_details[j+3].text) + '\n'
            write_to_file(file_handler, to_print)
            to_print = ""

def fetch_more_accounts_wait(driver, page_number_range_name):
    temp = driver.find_element_by_class_name(page_number_range_name)
    while '8' not in temp.text:
        sleep(1)
        temp = driver.find_element_by_class_name(page_number_range_name)
    temp = str(temp.text)
    max_number_of_pages = int(temp[temp.find('8'):temp.find('8')+2])
    return(max_number_of_pages)


def main():
    driver = start_session()
    driver.get(target_url)
    driver.find_element_by_name(name_username_entry).send_keys(user_name)
    driver.find_element_by_name(name_password_entry).send_keys(password)
    driver.find_element_by_name(name_login_button).click()
    driver.find_element_by_name(name_accounts_href).click()
    driver.find_element_by_name(name_agent_enquire_update_href).click()
    WebDriverWait(driver, 120).until(EC.title_contains(accounts_page_title))
    driver.find_element_by_name(name_fetch_more_accounts_button).click()
    max_number_of_pages = fetch_more_accounts_wait(driver, name_page_number_range)
    file_handler = open_file('inventory.txt', 'w')
    iterate_through_pages(driver, max_number_of_pages, file_handler)

if __name__ == "__main__":
    main()
