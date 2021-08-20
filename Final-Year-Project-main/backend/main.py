from typing import List
from fastapi import FastAPI, File, UploadFile, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from models import ChildModel
from config import cors, CHILD_IMG_DIR
import controller

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=cors['origins'], allow_credentials=True, allow_methods=cors['methods'], allow_headers=cors['headers'])

app.mount('/img/children', StaticFiles(directory=CHILD_IMG_DIR), name='children-images')

@app.post('/train/{mode}')
async def train(mode: str = 'known'):
    return await controller.train(mode)

@app.post('/upload-images')
async def upload(images: List[UploadFile] = File(...)):
    return await controller.upload(images)

@app.get('/delete-uploaded-images/{upload_id}')
def upload(upload_id: str):
    return controller.delete(upload_id)

@app.get('/search-results/{upload_id}/{mode}')
async def find(upload_id: str, mode: str):
    return await controller.find(upload_id, mode)

@app.post('/save-images/{upload_id}')
async def save(upload_id: str, child: ChildModel = Body(...)):
    # return {'uid': upload_id, 'child': child}
    return await controller.save(upload_id, child)

@app.get('/children-counts')
async def count():
    return await controller.children_counts()

