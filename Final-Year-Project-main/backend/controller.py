from fastapi.encoders import jsonable_encoder
from os import path, walk, mkdir, listdir
from shutil import move, rmtree as remove_dir_r
from uuid import uuid4
from config import *

from config import DB

from FaceRecognizer import model
from FaceRecognizer.config import allowed_image_types

children = DB['children']

async def upload(images):
    tmp_dir = path.join(TMP_IMG_DIR, str(uuid4()))
    while path.isdir(tmp_dir):
        tmp_dir = path.join(TMP_IMG_DIR, str(uuid4()))
    mkdir(tmp_dir)
    for img in images:
        loc = path.join(tmp_dir, img.filename)
        with open(loc, 'wb+') as fo:
            fo.write(img.file.read())
    return {'upload_id': path.basename(tmp_dir)}

def delete(tmp_dir):
    tmp_imgs_dir = path.join(TMP_IMG_DIR, tmp_dir)
    if path.isdir(tmp_imgs_dir):
        remove_dir_r(tmp_imgs_dir)
    return {'success': 1, 'msg': 'success.'}

async def save(tmp_dir, child):
    tmp_imgs_dir = path.join(TMP_IMG_DIR, tmp_dir)
    if not path.isdir(tmp_imgs_dir):
        return {'success': 0, 'error': 'uploaded id not found.'}
    if child.type=='unknown':
        delattr(child.info, 'name')
    new_child = await children.insert_one(jsonable_encoder(child))
    target_dir = path.join(CHILD_IMG_DIR, str(new_child.inserted_id))
    move(tmp_imgs_dir, target_dir)
    return {'success': 1, 'child_id': str(new_child.inserted_id)}

async def find(tmp_dir, mode):
    imgs_dir = path.join(TMP_IMG_DIR, tmp_dir)
    if not path.isdir(imgs_dir):
        return {'success': 0, 'error': 'upload id not found.'}
    images = []
    for root, dirs, files in walk(imgs_dir):
        for file in files:
            ext = '' if len(path.splitext(file)) < 2 else path.splitext(file)[1][1:]
            if ext in allowed_image_types:
                images.append({'path': path.join(imgs_dir, file)})
    mode = 'known' if mode=='in_knowns' else 'unknown'
    matches = await model.predict_from_images(images, mode)
    childs = await children.find({'_id': {'$in': matches}}).to_list(10000)
    for child in childs:
        directory = f'{CHILD_IMG_DIR}/{child["_id"]}'
        images = []
        if path.isdir(directory):
            for img in listdir(directory):
                ext = '' if len(path.splitext(img)) < 2 else path.splitext(img)[1][1:]
                if ext in allowed_image_types:
                    images.append(img)
        child.update({'images': images})
    return childs


async def train(mode):
    try:
        training_sets = await children.find({'type': mode}).to_list(10000)
        return await model.train(training_sets, mode)
    except Exception as e:
        return {'success': 0, 'error': e}

async def children_counts():
    known = await children.count_documents({'type': 'known'})
    unknown = await children.count_documents({'type': 'unknown'})
    return {'known': known, 'unknown': unknown}
