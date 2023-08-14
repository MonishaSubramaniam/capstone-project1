from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Test_Data import data
from Test_Locators import locators
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class Test_Project:
# Boot method to run Pytest using POM
   @pytest.fixture
   def startup(self):
      self.driver=webdriver.Chrome(service=Service(ChromeDriverManager(version="114.0.5735.90").install()))
      self.driver.maximize_window()
      yield
      self.driver.close()
# login testing
   def test_login_success(self, startup):
      self.driver.get(data.Data().url)
      try:
         cookie_before=self.driver.get_cookies()[0]['value']
         self.driver.implicitly_wait(10)
         self.driver.find_element(By.XPATH,locators.Locators().username_input_box).send_keys(data.Data().username)
         self.driver.find_element(By.XPATH,locators.Locators().password_input_box).send_keys(data.Data().valid_password )
         self.driver.find_element(By.XPATH,locators.Locators().submit_button).click()
         cookie_after=self.driver.get_cookies()[0]['value']
         assert cookie_before != cookie_after
         print("LOGIN SUCCESS WITH VALID PASSWORD")
      except:
         print("element missing")
        
    
   def test_login_failure(self, startup):
      self.driver.get(data.Data().url)
      self.wait=WebDriverWait(self.driver,20)
      self.driver.implicitly_wait(10)
      try:
         cookie_before=self.driver.get_cookies()[0]['value']
         self.driver.implicitly_wait(10)
         self.driver.find_element(By.XPATH,locators.Locators().username_input_box).send_keys(data.Data().username)
         self.driver.find_element(By.XPATH,locators.Locators().password_input_box).send_keys(data.Data().invalid_password )
         self.driver.find_element(By.XPATH,locators.Locators().submit_button).click()
         cookie_after=self.driver.get_cookies()[0]['value']
         assert cookie_before == cookie_after
         print("LOGIN FAILED WITH INVALID PASSWORD")
      except:
         print("element missing")

        

   def test_add_newemp(self,startup):
      self.wait=WebDriverWait(self.driver,10)
      self.driver.get(data.Data().url)
      self.driver.implicitly_wait(10)
      try:
         self.driver.find_element(By.XPATH,locators.Locators().username_input_box).send_keys(data.Data().username)
         self.driver.find_element(By.XPATH,locators.Locators().password_input_box).send_keys(data.Data().valid_password)
         self.driver.find_element(By.XPATH,locators.Locators().submit_button).click()
         self.driver.find_element(By.XPATH,locators.pimloc().pim).click()
         self.driver.find_element(By.XPATH,locators.pimloc().add).click()
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().fname))).send_keys(data.pim1().first_name)
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().mname))).send_keys(data.pim1().mid_name)
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().lname))).send_keys(data.pim1().last_name)
         save_btn=self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.pimloc().save)))
         save_btn.click()
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().nick))).send_keys(data.pim1().nick_name)
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().license))).send_keys(data.pim1().license_num)
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().other))).send_keys(data.pim1().other_num)
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().ssn))).send_keys(data.pim1().ssn_num)
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().sin))).send_keys(data.pim1().sin_num)
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().date))).send_keys(data.pim1().date)
         nation=self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.pimloc().nationality)))
         action=ActionChains(self.driver)
         action.click(on_element=nation).perform()
         afghan=self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.pimloc().afghan)))
         action=ActionChains(self.driver)
         action.click(on_element=afghan).perform()
         self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.pimloc().marital))).click()
         self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.pimloc().single))).click()
         self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.pimloc().female))).click()
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().dob))).send_keys(data.pim1().dob_value)
         save1_btn=self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.pimloc().save1)))
         save1_btn.click()
         print("NEW EMPLOYEE SAVED")
      except NoSuchElementException as e:
           print (e)
        
   def test_edit_employee(self,startup):
      self.wait=WebDriverWait(self.driver,15)
      self.driver.get(data.Data().url)
      self.driver.implicitly_wait(10)
      try:
         self.driver.find_element(By.XPATH,locators.Locators().username_input_box).send_keys(data.Data().username)
         self.driver.find_element(By.XPATH,locators.Locators().password_input_box).send_keys(data.Data().valid_password)
         self.driver.find_element(By.XPATH,locators.Locators().submit_button).click()
         self.driver.find_element(By.XPATH,locators.pimloc().pim).click()
         self.wait.until(EC.presence_of_element_located((By.LINK_TEXT,locators.pimloc().emp_list))).click()
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().emp_name))).send_keys(data.pim1().emp_name)
         search_btn=self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.pimloc().search_btn)))
         action=ActionChains(self.driver)
         action.move_to_element(search_btn).click(search_btn).perform()
         edit_btn=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().edit)))
         edit_btn.click()
         last_name=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().lname)))
         action=ActionChains(self.driver)
         last_name.clear()
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().lname))).send_keys(data.pim1().newlast_name)
         save1_btn=self.wait.until(EC.element_to_be_clickable((By.XPATH,locators.pimloc().save1)))
         save1_btn.click()
         print("EDITED SUCCESSFULLY")
      except TimeoutException as e:
            print (e)

   def test_delete_employee(self,startup):
      self.wait=WebDriverWait(self.driver,15)
      self.driver.implicitly_wait(5)
      self.driver.get(data.Data().url)
      try:
         self.driver.find_element(By.XPATH,locators.Locators().username_input_box).send_keys(data.Data().username)
         self.driver.find_element(By.XPATH,locators.Locators().password_input_box).send_keys(data.Data().valid_password)
         self.driver.find_element(By.XPATH,locators.Locators().submit_button).click()
         self.driver.find_element(By.XPATH,locators.pimloc().pim).click()
         self.wait.until(EC.presence_of_element_located((By.LINK_TEXT,locators.pimloc().emp_list))).click()
         self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().emp_name))).send_keys(data.pim1().emp_name)
         search_btn=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().search_btn)))
         action=ActionChains(self.driver)
         action.move_to_element(search_btn).click(search_btn).perform()
         checkbox=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().check)))
         checkbox.click()
         delete_btn=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().delete)))
         delete_btn.click()
         confirm_delete_btn=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.pimloc().confirm_delete)))
         confirm_delete_btn.click()
         
         print("DELETED SUCCESSFULLY")

      except TimeoutException as e:
            print (e)   
