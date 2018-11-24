# Local setup 
# cd("$(homedir())/Desktop/Machine Learning/Semester Project/")

# Description: This script beings with a path to the original 
#	bacteria images dataset and creates an expanded sample folder
#	of imaged Augmented.  
# 	This script can also be the area where we extract features.
#
# 	This script relies on Augmentor 
#	More on Augmentor here: https://github.com/mdbloice/Augmentor

import Augmentor 
from PIL import Image

Image.MAX_IMAGE_PIXELS = 1000000000 # Avoid Memory error 

# Configure Pipeline Source 
p = Augmentor.Pipeline("res/images_test")

# Choose the Augmentations and Transformations 
p.resize(probability=1.0, width=10, height=10)
	
	# This is the Area we can experiment on Feature Extraction or  

# Set processing and design configuration 
p.sample(20, multi_threaded=False) 
p.process() 