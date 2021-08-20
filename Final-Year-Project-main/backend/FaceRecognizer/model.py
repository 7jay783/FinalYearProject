from os import path, listdir
from sklearn import neighbors
from cv2 import imread
import face_recognition
import pickle5 as pickle


from .config import *

async def train(training_sets, mode):
    TRAINNER_FILE = TRAINNER_KNOWN_FILE if mode=='known' else TRAINNER_UNKNOWN_FILE
    labels = []
    train_encodings = []
    for t_set in training_sets:
        current_dir = path.join(CHILD_IMG_DIR, t_set['_id'])
        if path.isdir(current_dir):
            for file in listdir(current_dir):
                img_path = path.join(current_dir, file)
                if path.isdir(img_path):
                    continue
                ext = '' if len(path.splitext(img_path)) < 2 else path.splitext(img_path)[1][1:]
                if ext in allowed_image_types:
                    img_path = path.join(current_dir, file)
                    image = face_recognition.load_image_file(img_path)
                    face_bounding_boxes = face_recognition.face_locations(image)
                    if len(face_bounding_boxes) == 1: #train on image iff there is only one face
                        train_encodings.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                        labels.append(t_set['_id'])

    model = neighbors.KNeighborsClassifier(n_neighbors=preset['training_k_neighbors'], algorithm=preset['knn_algo'], weights=preset['knn_weights'])

    if len(train_encodings):
        model.fit(train_encodings, labels)
        with open(TRAINNER_FILE, 'wb') as f:
            pickle.dump(model, f)
        return {'success': 1, 'msg': f'trainning success on {len(train_encodings)} images.'}
    else:
        return {'success': 0, 'error': 'no image to train.'}


async def predict_from_images(images, mode):
    TRAINNER_FILE = TRAINNER_KNOWN_FILE if mode=='known' else TRAINNER_UNKNOWN_FILE
    print(TRAINNER_FILE)
    matches = []
    with open(TRAINNER_FILE, 'rb') as f:
        model = pickle.load(f)
    for image in images:
        img = imread(image['path'])
        face_locations = face_recognition.face_locations(img)
        faces_encodings = face_recognition.face_encodings(img, known_face_locations=face_locations)
        closest_distances = model.kneighbors(faces_encodings, n_neighbors=preset['prediction_k_neighbors'])
        possible_matches = []
        for i in range(len(face_locations)):
            possible_matches.append(closest_distances[0][i][0] <= preset['prediction_distance_threshold'])
        for pred, loc, rec in zip(model.predict(faces_encodings), face_locations, possible_matches):
            if rec:
                matches.append(pred)
    return matches  #array of ids of the matchings


def find_matches_in_video(video_url):
    pass