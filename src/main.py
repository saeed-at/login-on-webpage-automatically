import winwifi
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from loguru import logger
import subprocess
import re  

class AutoConnectWifi():
    def __init__(self):
        config = {}
        with open("data.txt") as file:
            for line in file:
                line = line[0:len(line)-1]
                key,value = line.split(': ')
                config[key] = value
        self.wifi_ssids = list(config['wifi names'].split(','))
        self.url = config['url']
        self.password = config['password']
        self.username = config['username']
        
    def scan_all_available_wifi(self):
        logger.info('Scanning all available WiFi...')
        self.available_wifi = []
        devices = subprocess.check_output(['netsh','wlan','show','network'])
        devices = devices.decode('ascii')
        string_ = re.findall('SSID.+\n', devices)
        for ssid in string_:
            s = re.findall(':.+\n', ssid)
            ssid_name = s[0][2:]
            self.available_wifi.append(ssid_name[0:(len(ssid_name)-2)])
        
    def connect(self):
        logger.info('Connectiing to WiFi...')
        flag = False
        for wifi_ssid in self.wifi_ssids:
            if wifi_ssid in self.available_wifi:
                winwifi.WinWiFi.connect(wifi_ssid)
                self.connected_wifi = wifi_ssid
                flag = True
                break
        return flag

    def login(self):
        logger.info('Logging in...')
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        enter = driver.find_element(By.ID, 'internetbutton')
        username.send_keys('saeed.alijani')
        password.send_keys('1376Enola')
        logger.info("Done!")
        enter.click()
        driver.close()
    

if __name__ == "__main__":
    auto_connect = AutoConnectWifi()
    auto_connect.scan_all_available_wifi()
    res = auto_connect.connect()
    if res:
        logger.info('Connected to %s' % auto_connect.connected_wifi)
        auto_connect.login()
    else:
        logger.error('No known WiFi found!...')
        #do not exit cmd window
        os.system("pause")
    
