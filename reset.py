#!/usr/bin/python3

# (c) 2020 @MrHctr
# Se proporciona sin garantía *de ningún tipo*, no se aceptan
# responsabilidades por uso *EN NINGÚN CASO*

import sys
import requests
import base64
import re

# Ajustar estos dos parámetros a los valores necesarios
ip='192.168.1.1'
password='password'

####################
user='1234'
host = 'http://' + ip + '/'
auth = user + ':' + password
sessionKey = base64.b64encode(auth.encode())
data = {'sessionKey': sessionKey, 'pass':''}
r = requests.post(host + 'login-login.cgi', data=data)

# Get cookies (interested in SESSION)
session = r.cookies
print(session['SESSION'])
result = requests.get(host + 'resetrouter.html', cookies=session)

# Extract "var sessionKey='nnnn'"

match=re.search(r"var sessionKey='([0-9]+)'", result.text)
sessionKey = match.group(1)
print(sessionKey)
params={'sessionKey':sessionKey}
result = requests.get(host + 'rebootinfo.cgi', params=params, cookies=session)
