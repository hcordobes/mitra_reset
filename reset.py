#!/usr/bin/python3

"""
2020 @MrHctr

Exención de responsabilidad
  Se proporciona sin garantía *de ningún tipo*, no se aceptan
  responsabilidades por uso *EN NINGÚN CASO*

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import requests
import base64
import re

# Ajustar estos dos parámetros a los valores necesarios
ip='192.168.1.1'
password='password'

####################
user = '1234'
host = 'http://' + ip + '/'
auth = user + ':' + password
sessionKey = base64.b64encode(auth.encode())
data = {'sessionKey': sessionKey, 'pass':''}
r = requests.post(host + 'login-login.cgi', data=data)

# Get cookies (interested in SESSION)
session = r.cookies
result = requests.get(host + 'resetrouter.html', cookies=session)

# Extract "var sessionKey='nnnn'"

match = re.search(r"var sessionKey='([0-9]+)'", result.text)
sessionKey = match.group(1)
params = {'sessionKey':sessionKey}
result = requests.get(host + 'rebootinfo.cgi', params=params, cookies=session)
