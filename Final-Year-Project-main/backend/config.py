from os import path
from sys import argv
from motor.motor_asyncio import AsyncIOMotorClient

BASE_DIR = path.dirname(path.realpath(argv[0]))

FACE_RECOGNIZER_DIR = path.join(BASE_DIR, 'FaceRecognizer')

BASE_IMG_DIR = path.join(FACE_RECOGNIZER_DIR, 'data', 'images')
CHILD_IMG_DIR = path.join(BASE_IMG_DIR, 'children')

TMP_DIR = path.join(BASE_DIR, 'storage', 'tmp')
TMP_IMG_DIR = path.join(TMP_DIR, 'images')

cors = {
    'origins': ['https://linux.vm:7150', 'https://api.domain.com'],
    'methods': ['*'],
    'headers': ['*']
}

db = {
    'host': 'linux.vm',
    'port': 27017,
    'user': 'admin',
    'password': '07860',
    'name': 'final-year-project'
}

DB_URL = f"mongodb://{db['user']}:{db['password']}@{db['host']}/?retryWrites=true&w=majority"
DB = AsyncIOMotorClient(DB_URL)[db['name']]
