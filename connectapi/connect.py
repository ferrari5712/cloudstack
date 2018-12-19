import urllib
import hmac
import base64
import hashlib
import urllib3

baseurl = 'http://192.168.194.31:8080/client/api?'
request = dict()
request['command'] = 'listUsers'
request['response'] = 'json'

