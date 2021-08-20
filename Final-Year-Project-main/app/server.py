import uvicorn

APP = 'main:app'
SSL = {
	'enable': True,
	'cert': '/home/moin/.certs/linux.vm/cert.pem',
	'key': '/home/moin/.certs/linux.vm/key.pem'
}

config = {
	'host': '0.0.0.0',
	'port': 7151,
	'log_level': 'info',
	'reload': True
}

if SSL['enable']==True:
	config.update({'ssl_certfile': SSL['cert'], 'ssl_keyfile': SSL['key']})

if __name__ == '__main__':
    uvicorn.run(APP, **config)

#uvicorn==0.14.0