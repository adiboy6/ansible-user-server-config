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

def populateAuthFile():
	cur = conn.cursor()
	cur.execute("SELECT * FROM auth_keys;")
	if cur is None:
		return
	os.system("sh clear_auth_file.sh")
	os.system("chmod u+x append_pub_key.sh")
	for record in cur:
		os.system("sh append_pub_key.sh " + str(record[2]) + " " + str(record[1]) + " "  + str(record[0]))# algo, key, host
	cur.close()
	conn.commit()

if __name__ == '__main__':	
	setupTable()
	populateAuthFile()
	conn.close()
