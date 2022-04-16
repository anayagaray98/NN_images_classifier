
from os import listdir
from numpy import asarray
from numpy import save
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


folder = 'images/dog/'

photos, labels = list(), list()

for file in listdir(folder):

	# determine class
	output = 0.0
	if file.startswith('dog'):
		output = 1.0

	photo = load_img(folder + file, target_size=(200, 200))

	photo = img_to_array(photo)

	photos.append(photo)
	labels.append


photos = asarray(photos)
labels = asarray(labels)

save('dogs_vs_cats_photos.npy', photos)
save('dogs_vs_cats_labels.npy', labels)
