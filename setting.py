import os

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

# Pathes
# path = "/Define/Your/Own/Paths/"
data_path = "."
# baseline_path = create_dir(path + "/Adversarial_Training/models/baselines")
# adversarial_path = create_dir(path + "/Adversarial_Training/models/adversarial")
# generation_path = create_dir(path + "/Adversarial_Training/figures/generation")
# activation_path = create_dir(path + "/Adversarial_Training/figures/activation")
# tsne_path = create_dir(path + "/Adversarial_Training/features")

# Experiment conditions
subject = 1
batch_size = 64
total_epoch = 5
n_noise = 400
learning_rate = 1e-5
window_size = 512
