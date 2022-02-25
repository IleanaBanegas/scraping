"""
@author: Eduardo Lopez
@email: eduardolopezlainez2001@gmail.com
@version: 1.0
"""

from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

#Funcion that get the content in the div html tag of the amount of pages indicated
def getData():
    data = []
    while True:
        page = driver.find_elements_by_xpath('//div[@class="box_generador"]//a')
        if len(page) < 13:
            break
        else:
            content = driver.find_elements_by_xpath('//div[@class="cont_emp"]')
            text_content = [i.text for i in content]
            data.extend(text_content)
            next_page = driver.find_element_by_xpath('//div[@class="box_generador"]//a[13]')
        
            next_page.click()
    
    return data

#Function that separate the content

    def separateData(data):
    agents = []
    address = []
    agents = []
    phones = []
    names = []
    
    for i in range(len(data)):
        columns = data[i].split("\n")
        names.append(columns[0])
        address.append(columns[1])
        agents.append(columns[2])
        phones.append(columns[3])
        
    return names, address, agents, phones 

    #Make a strip to get only the address values

def getAddress(data):
    address = []
    for i in range(len(data)):
        single_address = data[i].strip("Dirección:")
        address.append(single_address)

    return address

    #Make a strip to get only the agents values

def getAgents(data):
    agents = []
    for i in range(len(data)):
        agent = data[i].strip("Representante:")
        agents.append(agent)

    return agents 

    #Make a strip to get only the phones values

def getPhones(data):
    phones = []
    for i in range(len(data)):
        phone = data[i].strip("Teléfono:")
        phones.append(phone)
        
    return phones

path = os.getcwd()
driver_path = '{}\chromedriver.exe'.format(path)
driver = webdriver.Chrome(driver_path)
driver.get('https://www.perulicitaciones.com/empresas.html')   
data = getData()
name, addresses, agents, phones = separateData(data)
address = getAddress(addresses)
agent = getAgents(agents)
phone = getPhones(phones)
df = pd.DataFrame({"Empresa": name,"Dirección": address, "Representante": agent, "Teléfono": phone})
df.to_excel("Licitaciones-Scraping.xlsx")

df