import h5py


# import h5py

# # Open the HDF5 file
# file_path = 'Stocks_data/3IINFOLTD.NS.h5'
# h5_file = h5py.File(file_path, 'r')

# # List all the datasets in the file
# print("Datasets in HDF5 file:")
# for dataset_name in h5_file.keys():
#     print(dataset_name)

# # Close the HDF5 file
# h5_file.close()


# Open the HDF5 file
file_path = 'Stocks_data/3IINFOLTD.NS.h5'
h5_file = h5py.File(file_path, 'r')

# List all the groups and datasets in the file
print("Groups and Datasets in HDF5 file:")
for name in h5_file:
    print(name)

# Access a specific dataset in the file
dataset = h5_file['data/index']
data = dataset[()]  # Read the data into a variable

# Print the data
print("Data in the dataset:")
print(data)

# Close the HDF5 file
h5_file.close()

import h5py

# Open the HDF5 file
file_path = 'Stocks_data/3IINFOLTD.NS.h5'
h5_file = h5py.File(file_path, 'r')

# Explore the groups and datasets within the file
def explore_hdf5(file, path=''):
    if isinstance(file, h5py.Group):
        for key in file.keys():
            new_path = f"{path}/{key}"
            print(f"Group: {new_path}")
            explore_hdf5(file[key], new_path)
    elif isinstance(file, h5py.Dataset):
        print(f"Dataset: {path}")

# Call the function to explore the HDF5 file
explore_hdf5(h5_file)

# Close the HDF5 file
h5_file.close()

