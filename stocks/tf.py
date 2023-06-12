# import tensorflow as tf

# tf.add(1, 2).numpy()
# hello = tf.constant('Hello, TensorFlow!')
# print(hello.numpy())

import h5py

# Open the HDF5 file
file_path = 'saved_models/best_model.hdf5'
h5_file = h5py.File(file_path, 'r')

# List all the groups and datasets in the file
print("Groups and Datasets in HDF5 file:")
for name in h5_file:
    print(name)

# Access a specific dataset in the file
dataset = h5_file['saved_models/model_epoch_01.hdf5']
data = dataset[()]  # Read the data into a variable

# Print the data
print("Data in the dataset:")
print(data)

# Close the HDF5 file
h5_file.close()
