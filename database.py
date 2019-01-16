import os
import psycopg2
#TODO: Get string from env variables
conn = psycopg2.connect("postgres://izrkemjg:VFMiROGWySbuIBR0xqkdTbIvxKWREbuN@stampy.db.elephantsql.com:5432/izrkemjg")
def setupTable():
	cur = conn.cursor()
	try:
		cur.execute("CREATE TABLE auth_keys (host varchar PRIMARY KEY, pubkey varchar, algo varchar);")
	except psycopg2.ProgrammingError as error:
		print "Table exists, " + str(error)
	cur.close()
	conn.commit()

def checkUserKeyExists(host):
	cur = conn.cursor()
	cur.execute("SELECT * FROM auth_keys where host = '%s' limit 1;" % host)
	result = cur.fetchone()
	if result is None:
		cur.close()
		conn.commit()
		return False
	cur.close()
	conn.commit()
	return True

def findDiffKey():
	pass

host = "pelashchoudhary@Potato.local"
algo = "ssh-rsa"
pubkey = "AAAAB3NzaC1yc2EAAAADAQABAAABAQDfYV2zUUI4CMzQxAihs3zAxzDcYI2G1SARm9ChjV1AAIVnJ0S1FIyu1vsb+QRcJ1xhOIHcUvCui0+Lnww7myEH6iOSIH06I/Q10gt0POKJWcrpIJXD2Y6BKTmwZujVwX7EJAAi6gSU1O5BWGflYCdIKBuveJ8YlggySpPDUYWjp6LG4lzhzZX9qv8GYXXl5QLjb0g6hMd1pRG8uHioH8i8WzOR9i7kMAc/5tAAsDNtOr24nhe55lQwubWYR5hTyFKAhSlvIugmR+pkTukeLW9QStlFi9lf+xw//55pazSuCnPoPGX1oFtov1mUSNa5kjYe6ujHPYjZoobu0KnDx0hr" 

def updateKey(host, pubkey, algo):
	cur = conn.cursor()
	cur.execute("UPDATE auth_keys SET pubkey = '%s' where host = '%s';" % (pubkey, host))

	cur.close()
	conn.commit()

def insertKeys(host, pubkey, algo):
	if(checkUserKeyExists(host)):
		updateKey(host, pubkey, algo)
		return
	cur = conn.cursor()
	cur.execute("INSERT INTO auth_keys VALUES ('%s', '%s', '%s') ;" % (host, pubkey, algo))

	cur.close()
	conn.commit()
def populateAuthFile():
	cur = conn.cursor()
	cur.execute("SELECT * FROM auth_keys;")
	if cur is None:
		return
	os.system("sh clear_auth_file.sh")
	for record in cur:
		os.system("sh append_pub_key.sh " + str(record[2]) + " " + str(record[1]) + " "  + str(record[0]))# algo, key, host
	cur.close()
	conn.commit()

def getCentralAuthList():
	values = []
	cur = conn.cursor()
	cur.execute("SELECT * FROM auth_keys;")
	if cur is None:
		values
	for record in cur:
		values.append(list(record))
	cur.close()
	conn.commit()
	return values

def updateCentralDb():
	values = getCentralAuthList()	

def setupPython():
	return True	
if __name__ == '__main__':
	setupPython()	
	setupTable()
	#insertKeys(host, pubkey, algo)
	populateAuthFile()
	updateCentralDb()
	conn.close()
