from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from time import sleep

target_url = 'https://dopagent.indiapost.gov.in/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&__FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=3&BANK_ID=DOP&AGENT_FLAG=Y'
user_name = 'DOP.MI5600700400014'
password = 'ramurohan#105'
initial_title = 'Department of Post Agent Login : Login'


# find by name
find_name = 'AuthenticationFG.USER_PRINCIPAL'
find_password = 'AuthenticationFG.ACCESS_CODE'
find_login = 'Action.VALIDATE_RM_PLUS_CREDENTIALS_CATCHA_DISABLED'
find_accounts = 'HREF_Accounts'
find_agent_enquire_update = 'HREF_Agent Enquire & Update Screen'
find_next_page = 'Action.AgentRDActSummaryAllListing.GOTO_PAGE__'

find_page_number = 'CustomAgentRDAccountFG.AgentRDActSummaryAllListing_REQUESTED_PAGE_NUMBER'
page_number = '3'

# driver = webdriver.Chrome('/home/prajwal/VirtualENV/web-scraper/bin/chromedriver')
driver = webdriver.Firefox()

driver.get(target_url)
driver.find_element_by_name(find_name).send_keys(user_name)
driver.find_element_by_name(find_password).send_keys(password)
driver.find_element_by_name(find_login).click()
driver.find_element_by_name(find_accounts).click()
driver.find_element_by_name(find_agent_enquire_update).click()
sleep(2)
driver.find_element_by_name(find_page_number).send_keys(page_number)
sleep(2)
driver.find_element_by_name(find_next_page).click()
# WebDriverWait(driver, 30).until(EC.title_contains(intial_title))
