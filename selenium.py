# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 03:37:50 2018cl

@author: ynebh
"""

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time

import csv

import requests
from lxml import html
from bs4 import BeautifulSoup

with open ('company.csv','w') as file:
    column_name = ['Name','Area','Telephone','Address','Mobile','Contact_person','email','website']
    writer= csv.DictWriter(file, fieldnames=column_name)
    writer.writeheader()

    browser = webdriver.Chrome(executable_path='C:\\Users\\ynebh\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe')
    
    browser.get("https://infoline.com/ahmedabad/professionals-consultants/hospital-doctors/hospital-medical-centre/395?searchtext=hospital&FApplied=2:71")
    time.sleep(5)
    python_button = browser.find_element_by_class_name('mfp-close') #FHSU
    python_button.click()
    time.sleep(5)
    element_present = browser.find_element_by_class_name('cPaging')
    while (element_present != None):
        try:
            element_present = browser.find_element_by_class_name('cPaging')
            WebDriverWait(driver, timeout).until(element_present)
            element_present.click()
            time.sleep(10)
            element_present = browser.find_element_by_class_name('cPaging') #FHSU 
        except Exception as Attrib:
            print('Continue with no element')

        
        #python_button.click()
        #time.sleep(10)
        
        
    for company in browser.find_elements_by_class_name('company_infocon'):     
        r = requests.get(company.find_element_by_css_selector('a').get_attribute('href'))
        content = r.content
        soup = BeautifulSoup(content, "html.parser")
        
        #NAME 
        
        try:
            Name=soup.find("div", {"class": "left_box_details"}).find("h4")
            print(Name.text)
            Name_file = Name.text
        except AttributeError as Attrib:
                Name_file = 'Name.text'
                print('No Name')
        
        
        
        #Area 
        
        try:
            Area=soup.find("div",{"class":""}).find("p")
            print(Area.text)
            Area_file = Area.text
        except AttributeError as Attrib:
                print('No Area')
                Area_file = 'No Area'
        
        
        
        #Telephone
        try:
            Telephone = soup.find("span",{"class":"telephone"})
            print(Telephone.text)
            Telephone_file = Telephone.text
            
        except AttributeError as Attrib:
                print('No telephone')
                Telephone_file = 'No telephone'
        
        
        #Address
        try:
            Address = soup.find("span",{"itemprop":"streetAddress"})
            print(Address.text)
            Address_file = Address.text
        except AttributeError as Attrib:
                print('No Address')
                Address_file = Address.text
        
        
        """
        while(soup.find("span",{"itemprop":"telephone"}) != None):
            Mobile = soup.find("span",{"itemprop":"telephone"})
            print(Mobile.text)"""
        #print(soup.find_all('p').text)
        #soup.find("div", { "class" : "contact_bxtitle" })
        
        ## MOBILE 
        Mobile = soup.find("span",{"itemprop":"telephone"})
        try:
            Mobile = soup.find("span",{"itemprop":"telephone"})
            print(Mobile.text)
            Mobile_file = Mobile.text
        except AttributeError as Attrib:
                print('Company has no Mobile number')
                Mobile_file = 'No Mobile'
        
        
        
        #Contact_Person
        try:
            Contact_person = soup.find("div",{"itemtype":"http://schema.org/Person"})
            print(Contact_person.text)
            print(Contact_person.text)
            Contact_personfile = Contact_person.text
            print(Contact_personfile)
        except AttributeError as Attrib:
                print('Company has no Contact person')
                Contact_personfile = 'No person'
        
        
        #Email
        email = soup.find("span",{"itemprop":"email"})
        try:
            email = soup.find("span",{"itemprop":"email"})
            print(email.text)
            email_file = email.text
        except AttributeError as Attrib:
                print('Company has no email')
                email_file = 'No email'
        
        
        #Website
        try:
            website = soup.find("a",{"itemprop":"url"})
            print(website.text)
            website_file = website.text
        except AttributeError as Attrib:
                print('Company has no website')
                website_file = 'No website'
        
        
        
        
        
        #print(Contact_person.text)
        #print(email.text)
        #print(website.text)
        
        
        
        #print(Name.text)
        #print(Area.text)
        #print(Telephone.text)
        csr= {
              "Name": Name_file, "Area": Area_file,"Telephone": Telephone_file,
              "Address": Address_file,"Mobile": Mobile_file,
              "Contact_person": Contact_personfile,
              "email":email_file, "website":website_file 
              }
        #csr= {"Area": Area.text}
        
        #csr={"Area":Area.text}
        writer.writerow(csr)
