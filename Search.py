# Import Necessary Libraries

# Selenium for Webdrivers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# BeautifulSoup for HTML Page Scraping and Parsing
from bs4 import BeautifulSoup

# Regular Expression
import re

# Data Analysis functionalities
import pandas as pd

# To use operating system dependent functionality
import os

# Time for Time methods
import time


# Creating Bot
class searchBot:

    # Initialise the bot
    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Define Web-browser
        self.browser = webdriver.Firefox()



    # To close the browser
    def closeBrowser(self):
        self.browser.close()


    def login(self):

        # On Campus Job URL
        URL = "https://shibboleth2.asu.edu/idp/profile/SAML2/Unsolicited/SSO?providerId=https%3A%2F%2Fsso.brassring.com%2Fsso%2Fsaml%2FSAML2PageListener%2FAuthenticationRequestor.aspx%3FLocation%3D5495"

        # Open URL
        self.browser.get(URL)
        time.sleep(2)

        # Find Element to Click on On-Campus Job

        # Username Element
        username_element = self.browser.find_element_by_xpath("//input[@name='username']")
        username_element.clear()
        username_element.send_keys(self.username)

        # Password Element
        password_element = self.browser.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)

        # Enter to Login
        password_element.send_keys(Keys.RETURN)

        time.sleep(5)

    def searchKeyword(self,keyword):
        self.keyword = keyword

        # Sleep to make sure Page loads before reading element
        time.sleep(20)

        # Input Box for keyword
        keyword_element = self.browser.find_element_by_xpath("//input[@name='keyWordSearch']")
        keyword_element.clear()
        keyword_element.send_keys(self.keyword)

        # Press Search
        Search_btn = self.browser.find_element_by_xpath("//button[@id='searchControls_BUTTON_2']")
        Search_btn.click()





JobSearch = searchBot("username","password")

#Call without any arguements
JobSearch.login()

#Call with Keyword as an arguement
JobSearch.searchKeyword("Grader")
