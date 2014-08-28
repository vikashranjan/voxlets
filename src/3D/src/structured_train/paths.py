'''
This module is purely here to store the paths to the data associated with all this structured prediction
'''

import os

# per-view data paths
base_path = os.path.expanduser("~/projects/shape_sharing/data/3D/basis_models/")
model_features = base_path + 'structured/features/'

# paths to do with the dataset as a whole
models_list = base_path + 'databaseFull/fields/models.txt'
split_path = base_path + 'structured/split.mat'

# locations of the combined features
combined_features_path = base_path + 'structured/combined_features/'
combined_test_features = combined_features_path + 'test.mat'
combined_test_features_small = combined_features_path + 'test_small.mat'
combined_train_features = combined_features_path + 'train.mat'
combined_train_features_small = combined_features_path + 'train_small.mat'

# paths for the random forest models
model_config = './data/models_config.yaml'
rf_folder_path = "./data/models/"
rf_folder_path_small = "./data/models_small/"

# paths for the sparse results
results_folder = "./data/results/"
results_folder_small = "./data/results_small/"

# paths for the dense predictions
#dense_predictions = base_path + 