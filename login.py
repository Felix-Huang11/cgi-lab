#!/usr/bin/env python3
import templates
import cgi, cgitb
import secret
# import Cookie

print('Content-Type: text/html')
form = cgi.FieldStorage()
n = form.getvalue('username')
p  = form.getvalue('password')

if(n == secret.username and p == secret.password):
	print("Set-Cookie:username = " + n + ";")
	print("Set-Cookie:password = " + p + ";\r\n")
	# cookie["username"] = n
	# cookie["password"] = p
	print(templates.secret_page(n, p))
print()
print(templates.login_page())

print("")
print("")
print("username you entered:  %s, password you entered: %s" % (n, p))