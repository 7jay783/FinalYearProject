from os import path


FACE_RECOGNIZER_DIR = path.dirname(__file__)

CHILD_IMG_DIR = path.join(FACE_RECOGNIZER_DIR, 'data', 'images', 'children')

TRAINNER_DIR = path.join(FACE_RECOGNIZER_DIR, 'data', 'trainner')

TRAINNER_KNOWN_FILE = path.join(TRAINNER_DIR, 'children-known.knn.clf')
TRAINNER_UNKNOWN_FILE = path.join(TRAINNER_DIR, 'children-unknown.knn.clf')

allowed_image_types = ['png', 'jpg', 'jpeg']

preset = {
	'knn_algo': 'ball_tree',
	'training_k_neighbors': 2,
	'prediction_k_neighbors': 1,
	'prediction_distance_threshold': 0.5,
	'knn_weights': 'distance'
}





