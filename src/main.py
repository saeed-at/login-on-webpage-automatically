import winwifi
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from loguru import logger
import subprocess
import re  

class AutoConnectWifi():
    def __init__(self, wifi_ssids, url, password, username):
        self.wifi_ssids = wifi_ssids
        print(self.wifi_ssids)
        self.url = url
        self.password = password
        self.username = username
        
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
    auto_connect = AutoConnectWifi(['Wi-Fi 5GHz', 'Dir-615'], 'https://internet.aut.ac.ir/', '1376Enola', 'saeed.alijani')
    auto_connect.scan_all_available_wifi()
    res = auto_connect.connect()
    if res:
        auto_connect.login()
    else:
        logger.error('No known WiFi found!...')
    