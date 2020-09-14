'''Do the Daily Health Check.

'''

import time
from selenium.webdriver import Firefox
from password import get_netid, get_password

browser = Firefox()
browser.get(
  'https://yalesurvey.ca1.qualtrics.com/jfe/form/SV_eFnltn7gS5xctc9?Type=checkin'
)

browser.implicitly_wait(5)
username = browser.find_element_by_id('username')
username.send_keys(get_netid())
password = browser.find_element_by_id('password')
password.send_keys(get_password())
password.submit()

browser.implicitly_wait(5)
coming_to_campus = browser.find_element_by_id('QID1-3-label')
coming_to_campus.click()
coming_to_campus = browser.find_element_by_id('NextButton')
coming_to_campus.click()

browser.implicitly_wait(5)
coming_to_campus = browser.find_element_by_id('QID19-2-label')
coming_to_campus.click()
coming_to_campus = browser.find_element_by_id('NextButton')
coming_to_campus.click()

browser.implicitly_wait(5)
end = browser.find_element_by_id('EndOfSurvey')
time.sleep(.5)
browser.close()
