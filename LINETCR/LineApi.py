
# -*- coding: utf-8 -*-
from Api import Poll, Talk, channel
from lib.curve.ttypes import *
import requests
import shutil
import json
from random import randint

def def_callback(str):
    print(str)

class LINE:

  mid = None
  authToken = None
  cert = None
  channel_access_token = None
  token = None
  obs_token = None
  refresh_token = None


  def __init__(self):
    self.Talk = Talk()
    self._session = requests.session() 
#    self._headers = {'X-Line-Application': 'DESKTOPMAC 10.10.2-YOSEMITE-x64    MAC 4.5.0'} 
    self._headers = {'X-Line-Application': 'CHROMEOS 8.2.1 NADYA-TJ x64'}    
    

  def login(self, mail=None, passwd=None, cert=None, token=None, qr=False, callback=None):
    if callback is None:
      callback = def_callback
    resp = self.__validate(mail,passwd,cert,token,qr)
    if resp == 1:
      self.Talk.login(mail, passwd, callback=callback)
    elif resp == 2:
      self.Talk.login(mail,passwd,cert, callback=callback)
    elif resp == 3:
      self.Talk.TokenLogin(token)
    elif resp == 4:
      self.Talk.qrLogin(callback)
    else:
      raise Exception("invalid arguments")

    self.authToken = self.Talk.authToken
    self.cert = self.Talk.cert
    self._headers = {
#              'X-Line-Application': 'DESKTOPMAC 10.10.2-YOSEMITE-x64    MAC 4.5.0', 
#              'X-Line-Application': 'DESKTOPMAC 10.10.2-YOSEMITE-x64 MAC 4.5.1', 
              'X-Line-Application': 'CHROMEOS 8.2.1 NADYA-TJ x64', 
              'X-Line-Access': self.authToken, 
              'User-Agent': 'Line/8.2.1'
   }
   
    self.Poll = Poll(self.authToken)
    self.channel = channel.Channel(self.authToken)
    self.channel.login()	
    self.mid = self.channel.mid
    self.channel_access_token = self.channel.channel_access_token
    self.token = self.channel.token
    self.obs_token = self.channel.obs_token
    self.refresh_token = self.channel.refresh_token


  """User"""
  
