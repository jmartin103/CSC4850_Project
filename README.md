Julia Project 

Goal) We want to perform a statistical analysis on our data using the traditional Artificial Neural Netowork. To calirfy, our Neural Network will not be Convolution. Therefore, the opportunity to extract features will be the Augmentors job. 
Mocha's job is to use our reduced images to form a netowork. 


## The Architecture

### Augmentor - Python 
Augmentor is a image augmentation library build for extracting samples. Because of this is will be perfect for out project. 
Readmore about it here: https://augmentor.readthedocs.io/en/master/userguide/mainfeatures.html?highlight=resize		

### Mocha - Julia 
Once we have collected data we will use them as inputs and begin building the Neural netowork in Julia. 

Using our spreadsheet data we will is if we can train out network from certain features and see if there is a correlation between certain values in our network. 

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
***11/17/2018 - *** I have accomplished processing the files and creating samples. Now I will be trying to learn how to use Mocha with julia. This is the main Neural Network Library. 

