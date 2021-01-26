#!/usr/bin/env python3

import os
import json


# print('Content-Type: text/html')
# print('Content-Type: application/octet-stream')
# print('Content-Type: application/json')
# print()
# print(json.dumps(dict(os.environ), indent=2))

print('Content-Type: text/html')
print()

print('''
	<!DOCTYPE html>
	<html>
	<head>
	<title></title>
	</head>
	<body>
	<h1> Query Parameters</h1>
	<ul>
	''')

for para in os.environ['QUERY_STRING'].split('&'):
	(name, value) = para.split('=')
	print(f"<li><em>{name}</em> = {value} </li>")

print('''
	</ul>
	<br />
	<p>
	''')
browser = os.environ['HTTP_USER_AGENT']
print(f"Browser: {browser}")
print('''
	</p>
	</body>
	</html>
	''')




