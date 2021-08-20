import uvicorn

HOST = '0.0.0.0'
PORT = 7151
APP = 'main:app'

certs_dir = '/home/moin/.certs/linux.vm/'

SSL = {'enable': True, 'cert': certs_dir+'cert.pem', 'key': certs_dir+'key.pem'}

if __name__ == '__main__':
    uvicorn.run(APP, host=HOST, port=PORT, log_level='info', reload=True, ssl_certfile=SSL['cert'], ssl_keyfile=SSL['key'])