import time
import random
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless")
#option.add_argument("disable-gpu");
browser = webdriver.Chrome(executable_path=r'/home/srujan/chromedriver', chrome_options=option)



df1 = pd.read_csv('Indian-Female-Names.csv', delimiter=',')
df2 = pd.read_csv('Indian-Male-Names.csv', delimiter=',')
# User list comprehension to create a list of lists from Dataframe rows
females = [list(row) for row in df1.values]
males = [list(row) for row in df2.values]

try:
    for i in range(1):
        #print(i,end=",")
        browser.get("https://docs.google.com/forms/d/e/1FAIpQLScPT1grJW3MifAPCm9TOS1X8C8dbRrhkiStXm1WC7OYwRa_Yg/viewform")

        text = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput");
        print(len(text))
        rc = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper");
        submit = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

        campus = random.randint(1,3)
        year = random.randint(2016,2019)
        psrn = random.randint(1,99999)
        ppsrn = str(psrn)
        while(len(ppsrn)<5):
            ppsrn = '0'+ppsrn
        srn = "PES"+str(campus)+str(year)+str(ppsrn)

        if(i%10):
            n1 = random.choice(females)
            n2 = random.choice(males)
        else:
            n2 = random.choice(females)
            n1 = random.choice(males)

        name = n1[0]+' '+n2[0]
        email = name.replace(' ','').replace('@','').replace('.','') + '@gmail.com'

        text[0].send_keys(email)
        text[1].send_keys(name)
        text[2].send_keys(srn)

        rc[campus].click()
        rc[3].click()


        #submit.click()
except:
    browser.close()
#browser.close()
