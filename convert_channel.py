import h5py
import numpy as np

file_name = 'resnet152_weights_tf.h5'
group_name = 'conv1/conv1_W_1:0' # group inside file_name that u want to change

f = h5py.File(file_name)

sliding_height = 10 # new_shape variable
data = f[group_name]
data = np.asarray(data)

new_data = np.zeros((7, 7, 2*sliding_height, 64), float)

for i in range(len(data)):
    for j in range(len(data[i])):
        old_len = len(data[i][j][0])
        for l in range(old_len):
            avg = 0.0
            for k in range(len(data[i][j])):
                avg += data[i][j][k][l]
     
            avg /= len(data[i][j])
            for k in range(2*sliding_height):
                new_data[i][j][k][l] = avg

del f[group_name]
dset = f.create_dataset(group_name, data=new_data)
f.close()
