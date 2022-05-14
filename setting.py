# Import API
import os

# To make a folder
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

data_path = "/Define/Your/Own/Paths/"

# Hyperparameter settings
subject = 1 # subject
batch_size = 64
total_epoch = 5
n_noise = 400
learning_rate = 1e-5
window_size = 512
