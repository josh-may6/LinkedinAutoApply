import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


def next_button():
    # Below is a good solution for attribute values ## Does not work for "Review" button at the end though
    # button_next = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Continue to next step"]')))
    button_next = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")))
    button_next.click()


def disability_fill_out():
    disability_dropdown = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                          "#text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-8529494308693305758-multipleChoice")))
    disability_dropdown.click()
    disability_status = driver.find_element(By.XPATH,
                                            '//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-8529494308693305758-multipleChoice"]/option[3]')
    disability_status.click()


def veteran_fill_out():
    vet_dropdown = driver.find_element(By.CSS_SELECTOR,
                                       "#text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-3242243028264639378-multipleChoice")
    vet_dropdown.click()
    vet_status = driver.find_element(By.XPATH,
                                     '//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-3242243028264639378-multipleChoice"]/option[4]')
    vet_status.click()


def race_fill_out():
    race_status = Select(driver.find_element(By.CSS_SELECTOR,
                                             "#text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-4449099919134206644-multipleChoice"))
    race_status.select_by_visible_text("White")


def gender_fill_out():
    gender_choice = Select(driver.find_element(By.CSS_SELECTOR,
                                               "#text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-2472500748199245496-multipleChoice"))
    gender_choice.select_by_visible_text("Male")


def linkedin_profile():
    linkedin_entry = driver.find_element(By.CSS_SELECTOR,
                                         "#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-2600930713790599177-text")
    linkedin_entry.send_keys("https://www.linkedin.com/in/josh-maitre-real-estate/")


def state_of_residence():
    select_state = Select(driver.find_element(By.CSS_SELECTOR,
                                              "#text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-3140685035554104450-multipleChoice"))
    select_state.select_by_visible_text("Oregon")
    working_state = Select(driver.find_element(By.CSS_SELECTOR,
                                               "#text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-689511965420783316-multipleChoice"))
    working_state.select_by_visible_text("Oregon")


def upwork_questions():
    question1 = Select(driver.find_element(By.CSS_SELECTOR,
                                           "#text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-6115051625215194434-multipleChoice"))
    question1.select_by_visible_text("No")
    question2 = Select(driver.find_element(By.CSS_SELECTOR,
                                           "#text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-911662309926433275-multipleChoice"))
    question2.select_by_visible_text("He/Him/His")
    white = driver.find_element(By.XPATH,
                                '//*[@id="checkbox-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-7677932225865587886-multipleChoice"]/div[7]/label')
    white.click()
    man = driver.find_element(By.XPATH,
                              '//*[@id="checkbox-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-64797486524054012-multipleChoice"]/div[2]/label')
    man.click()
    straight = driver.find_element(By.XPATH,
                                   '//*[@id="checkbox-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-120490453840911378-multipleChoice"]/div[3]/label')
    straight.click()
    no_disability = driver.find_element(By.XPATH,
                                        '//*[@id="checkbox-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-4313532713306500168-multipleChoice"]/div[2]/label')
    no_disability.click()
    not_vet = driver.find_element(By.XPATH,
                                  '//*[@id="checkbox-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3739296922-882744458563950711-multipleChoice"]/div[2]/label')
    not_vet.click()


LINKEDIN_USER = os.environ["LINKEDIN_USER"]
LINKEDIN_PASS = os.environ["LINKEDIN_PASS"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    url="https://www.linkedin.com/jobs/search/?currentJobId=3739296922&distance=50&f_AL=true&geoId=101147714&keywords=Python%20Developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")

# Wait to load page then click Sign in
sign_in_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")))
sign_in_button.click()
# Username or Email
username = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
username.send_keys(LINKEDIN_USER)
# Password
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys(LINKEDIN_PASS)
# Press Sign in Button
enter_sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
enter_sign_in.click()
# Wait for page to load. Find list of Jobs(element) on Page
wait = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-view.jobs-search-results__list-item")))
job_objects = driver.find_element(By.CSS_SELECTOR, ".ember-view.jobs-search-results__list-item")
job_objects.click()
easy_apply = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-apply-button--top-card")))
easy_apply.click()
time.sleep(5)
next_button()
next_button()
disability_fill_out()
veteran_fill_out()
race_fill_out()
gender_fill_out()
next_button()
state_of_residence()
linkedin_profile()
upwork_questions()
next_button()
