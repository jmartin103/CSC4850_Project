# Description: This script is responsible to coverting your
# 	The from Augmentor into a format that can be used in Julia. 
#	In my case, it is HDF5. 

using CSV
using HDF5

# Lets try to convert the jpeg into something else. 

const width = 10 
const height = 10
const channels = 3 
const batch_size = 100


datasets = [("train", ["data_batch_$i.bin" for i in 1:5]),
            ("test", ["test_batch.bin"])]

for (key, sources) in datasets
	h5open("$key.hd5", "w") do h5
		dset_data = d_create(h1, "data", datatype(Float32), 
			dataspace(width, height, channels, batch_size * length(sources)))
		dset_label = d_create(h5, "label", datatype(Float32), 
			dataspace(1, batch_size * length(sources)))
end
