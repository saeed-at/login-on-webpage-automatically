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
        for wifi_ssid in wifi_ssids:
            if wifi_ssid in self.available_wifi:
                winwifi.WinWiFi.connect(wifi_ssid)
                flag = True
                break
        return flag


a = AutoConnectWifi(['Wi-Fi 5GHz'], 'https://google.com', 'saeed', '1236') 
a.scan_all_available_wifi()
