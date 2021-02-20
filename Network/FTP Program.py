# Honestly this is super simple.
from ftplib import FTP

host = '195.201.160.55'
username = 'kobi@weeb.kobi.lol'
password = 'kobioof.com'

with FTP(host=host) as ftp:
	ftp.login(user=username, passwd=password)
	a = ftp.dir()
	print(a)