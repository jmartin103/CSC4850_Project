
# Description: This file will read from the output folder generated by 
#	preprocessing.py and feed it though an Artifical Neutral Netowkr. 
# 	Please use read the following link, it will be helpful 
#
#	https://mochajl.readthedocs.io/en/latest/tutorial/mnist.html#preparing-the-data

## Configuration and Package Loading

using Mocha 


## Building the Network 

data_layer = HDF5DataLayer(name="train-data", source="\res\images_test\hdf5\data.txt", 
	batch_size=64, shuffle=true) 

convolutional_layer = ConvolutionLayer(name="conv-1",n_filter=20,kernel=(5,5), 
	bottoms=[:data_layer],tops=[:convolutional_layer])

pool_layer = PoolingLayer(name="pool1",kernel=(2,2),stride=(2,2),
	bottoms=[:convolutional_layer],tops=[:pool_layer])

convolutional_layer_2 = ConvolutionLayer(name="conv2",n_filter=50,kernel=(5,5),
	bottoms=[:pool_layer],tops=[:convolutional_layer_2])

pool_layer_2 = PoolingLayer(name="pool2",kernel=(2,2),stride=(2,2),
	bottoms=[:convolutional_layer_2],tops=[:pool_layer_2])

inner_product_layer	= InnerProductLayer(name="ip1",output_dim=500,neuron=Neurons.ReLU(),
	bottoms=[:pool_layer_2], tops=[:inner_product_layer])

inner_product_layer_2 = InnerProductLayer(name="ip2",output_dim=10,
	bottoms=[:inner_product_layer], tops=[:inner_product_layer_2])

loss_layer = SoftmaxLossLayer(name="loss", bottoms=[:inner_product_layer_2, :label])

backend = DefaultBackend()
init(backend)

common_layers = [convolutional_layer, pool_layer, convolutional_layer_2, 
	pool_layer_2, inner_product_layer, inner_product_layer_2]

net = Net("My Network", backend, [data_layer, common_layers..., loss])