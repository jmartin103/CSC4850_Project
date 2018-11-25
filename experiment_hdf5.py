
from random import shuffle
import glob
import numpy as np 
import h5py 
import cv2

shuffle_data = True  # shuffle the addresses before saving

hdf5_path = 'res/dataset.hdf5'  # address to where you want to save the hdf5 file
train_path = 'res/images_test/output/*.jpg'
# read addresses and labels from the 'train' folder
addrs = glob.glob(train_path)
print(addrs[0])

labels = [1 if 'PIL-2'  in addr else 0 for addr in addrs ] # For sake of learning using only two labels 

print(labels)


"""
labels = [0 if 'cat' in addr else 1 for addr in addrs]  # 0 = Cat, 1 = Dog
# to shuffle data
if shuffle_data:
    c = list(zip(addrs, labels))
    shuffle(c)
    addrs, labels = zip(*c)
    
# Divide the hata into 60% train, 20% validation, and 20% test
train_addrs = addrs[0:int(0.6*len(addrs))]
train_labels = labels[0:int(0.6*len(labels))]
val_addrs = addrs[int(0.6*len(addrs)):int(0.8*len(addrs))]
val_labels = labels[int(0.6*len(addrs)):int(0.8*len(addrs))]
test_addrs = addrs[int(0.8*len(addrs)):]
test_labels = labels[int(0.8*len(labels)):]
"""

# Tensor-flow data order 
# (number of data, image_height, image_width, image_depth)
data_shape = (len(addrs), 224, 224, 3) 

hdf5_file = h5py.File("C:/Users/trimo/Desktop/Machine Learning/Semester Project/res/images_test/hdf5/texthdf.hdf5", mode="w")

hdf5_file["label"]= "my label" 

hdf5_file.create_dataset("data", data_shape, np.int8)

# Loop over addresses
for i in range(len(addrs)) : 

	addr = addrs[i]
	img = cv2.imread(addr)
	img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)
	# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	#save the image
	hdf5_file["data"][i] = img
