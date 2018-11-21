#Semester Project 

Goal) We want to perform a statistical analysis on our data using the traditional Artificial Neural Netowork. To calirfy, our Neural Network will not be Convolution. Therefore, the opportunity to extract features will be the Augmentors job. 
Mocha's job is to use our reduced images to form a netowork. 


## The Architecture

### Augmentor - Python 
Augmentor is a image augmentation library build for extracting samples. Because of this is will be perfect for out project. 
Readmore about it here: https://augmentor.readthedocs.io/en/master/userguide/mainfeatures.html?highlight=resize		

### Mocha - Julia 
Once we have collected data we will use them as inputs and begin building the Neural netowork in Julia. 

Using our spreadsheet data we will is if we can train out network from certain features and see if there is a correlation between certain values in our network. 

**Note:** The res/images is missing because it contains sensitive data. ***PLEASE MAKE SURE YOU DON'T PUSH ANY REAL DATA!!!!***

## Journal 
---
***11/17/2018***- Just scrapped the Hough Circle Transform idea of extracting the slither of the images. I'm not trying to be original anymore. Project is due in 2 weeks, I am trying to learn. 
Step1) Install Augmentor in 

##### issue 1) - The error I encountered when installing Augmentor where that the files where too big. 

```
DecompressionBombWarning: Image size (103910400 pixels) exceeds limit of 89478485 pixels, could be decompression bomb DOS attack.
  DecompressionBombWarning)
```
**Solved:** 
```
from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000

#source: https://github.com/zimeon/iiif/issues/11
```
##### issue 2) - "IndexError: There are no operations associated with this pipeline" 

Solved: Just need to add operations like `p.rotate`, or `p.zoom`. This library is called Augmentor for a reason, so you know this is a requirement. 

##### Issue 3) - When I run the file, I get a "RuntimeError: I can't start new thread." Or Memory error. 

Depending on whether multi_threading is True or False

**Solved:** The issue is with my laptop. The damn thing ran out of memory. Now I really regret getting the touch screen with tradeoff to low memory. Ughhh. 

--- 
***11/17/2018 -*** I have accomplished processing the files and creating samples. Now I will be trying to learn how to use Mocha with julia. This is the main Neural Network Library. 

***11/19/2018 -*** Went hiking in Columbus Georgia yesterday, it was peaceful. Anyways, now I am back on this project. I must learn 2 things.
	#1) How to convert my image data into HD5 format
	#2) How to use this HD5 format with the network. 

WTF is a tensor? Reading on the HDF5DataLayer componenet in Mocha suggest that "Each dataset in the HDF5 file should be a N-dimensional tensor." 

I just learend that a tesor is represented similar to a vector/matrix, the main differnces is that a tensor is in context of a bigger structure and is connected with other tensors. If a variant tensor changes, its covariant tensor changes as well. 

***11/19/2018 -*** I just started building the network. I am following the MNIST tutorial: 	https://mochajl.readthedocs.io/en/latest/tutorial/mnist.html. 

So far I have build a couple "Layers"
1. A HDF5DataLayer 
	- Supposedly this can be a text file with paths of corresponding HDF5 files. 
	- By convention, this layer will look for [:data] and [:label] in oyur HDF5 files.
	- These will be defined in your "bottoms" section, note how we left those properies out. 
2. A ConvolutationLayer 
	- This is the first layer that processes the images. Convolution is the process -
	- scanning an image to derive features. It creates an identical matrix whose values
	- have been determined via algorithm. 
3. A PoolingLayer
	- I think this layer is responsible to reduce the size of your data. I am not sure. 
4. Inner ProductLayer
	- This is a simple layer an innder product (a, b ,c)(x, y, z) = a scalar(ac + by + cz)

Forward: Before, trying to figure out how to solve a neural network, I need to finalize how I swill save data. 