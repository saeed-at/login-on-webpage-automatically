import winwifi
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import os
from loguru import logger
import subprocess
import re
import time

class AutoConnectWifi():
    def __init__(self):
        """_summary_: Initialize the class
            read url, username, password, wifi_ssids from config.txt file and save them as class variables.
            url is the url of the website to login.
            username and password are the username and password of the user.
            wifi_ssids is the list of known wifi ssid's to connect to with each startup.
        """
        config = {}
        with open("config.txt") as file:
            for line in file:
                line = line[0:len(line)]
                key,value = line.split(': ')
                config[key] = value
        self.wifi_ssids = list(config['wifi names'].split(','))
        self.url = config['url']
        self.password = config['password']
        self.username = config['username']

    def scan_all_available_wifis(self):
        """_summary_: Scan all available wifi and save them as a list of strings and stores in self.available_wifis variable.
        """
        logger.info('Scanning all available WiFi...')
        self.available_wifis = []
        devices = subprocess.check_output(['netsh','wlan','show','network'])
        devices = devices.decode('ascii')
        string_ = re.findall('SSID.+\n', devices)
        for ssid in string_:
            s = re.findall(':.+\n', ssid)
            ssid_name = s[0][2:]
            self.available_wifis.append(ssid_name[0:(len(ssid_name)-2)])

    def connect(self):
        """_summary_: Connect to the wifi with the given ssid.

        :return: if wifinames is in available_wifis, connect to the wifi with the given ssid.
        :rtype: bool
        """
        logger.info('Connectiing to WiFi...')
        flag = False
        for wifi_ssid in self.wifi_ssids:
            if wifi_ssid in self.available_wifis:
                winwifi.WinWiFi.connect(wifi_ssid)
                self.connected_wifi = wifi_ssid
                flag = True
                break
        return flag

    def login(self):
        """_summary_: Login to the website with the given username and password.
        """
        logger.info('Logging in...')
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome()
        driver.get(self.url)
        
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        enter = driver.find_element(By.ID, 'internetbutton')
        username.send_keys(self.username)
        password.send_keys(self.password)
        driver.close()
        logger.info("Done!")
    

if __name__ == "__main__":
    auto_connect = AutoConnectWifi()
    auto_connect.scan_all_available_wifis()
    res = auto_connect.connect()
    if res:
        logger.info('Connected to %s' % auto_connect.connected_wifi)
        auto_connect.login()
    else:
        logger.error('No known WiFi found!...')
        #do not exit cmd window
        os.system("pause")
    

