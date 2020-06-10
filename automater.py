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
#option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless")
#option.add_argument("disable-gpu");
browser = webdriver.Chrome(executable_path=r'/home/srujan/chromedriver', chrome_options=option)


def is_ascii(s):
    return all(ord(c) < 128 for c in s)

df1 = pd.read_csv('Indian-Female-Names.csv', delimiter=',')
df2 = pd.read_csv('Indian-Male-Names.csv', delimiter=',')
females = [list(row) for row in df1.values]
males = [list(row) for row in df2.values]

for i in range(20):
    try:
        browser.get("https://docs.google.com/forms/d/e/1FAIpQLScPT1grJW3MifAPCm9TOS1X8C8dbRrhkiStXm1WC7OYwRa_Yg/viewform")

        text = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput");
        rc = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper");
        submit = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

        campus = random.randint(1,3)
        year = random.randint(2016,2019)
        psrn = random.randint(1,99999)
        ppsrn = str(psrn)
        while(len(ppsrn)<5):
            ppsrn = '0'+ppsrn
        srn = "PES"+str(campus)+str(year)+str(ppsrn)

        while(True):
            if(i%10):
                n1 = random.choice(females)
                n2 = random.choice(males)
            else:
                n2 = random.choice(females)
                n1 = random.choice(males)
            if is_ascii(n1[0]) and is_ascii(n2[0]):
                break

        name = n1[0]+' '+n2[0]
        email = name.replace(' ','').replace('@','').replace('.','').replace('/','') + '@gmail.com'

        text[0].send_keys(email)
        text[1].send_keys(name)
        text[2].send_keys(srn)

        rc[campus-1].click()
        rc[3].click()

        submit.click()
        print(i)
    except:
        pass

#browser.close()
