# =========================
# 1) setari & importuri
# =========================
import warnings
warnings.filterwarnings('ignore')

import os
os.environ['tf_enable_onednn_opts'] = '0'
os.environ['tf_cpp_min_log_level'] = '2'

import random
import numpy as np
import tensorflow as tf
import urllib.request
import tarfile
import shutil

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# =========================
# 2) reproducibilitate
# =========================
seed_value = 42
random.seed(seed_value)
np.random.seed(seed_value)
tf.random.set_seed(seed_value)

# =========================
# 3) hiperparametri de baza
# =========================
batch_size = 32
n_epochs = 5
img_rows, img_cols = 224, 224
input_shape = (img_rows, img_cols, 3)

# =========================
# 4) locul unde descarci / extragi
# =========================
base_dir = r"c:\dl"  # <- schimba dupa preferinta (ex. d:\data)
os.makedirs(base_dir, exist_ok=True)

dataset_url = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "ZjXM4RKxlBK9__ZjHBLl5A/aircraft-damage-dataset-v1.tar"
)
tar_filename = "aircraft_damage_dataset_v1.tar"
tar_path = os.path.join(base_dir, tar_filename)

extract_dir = os.path.join(base_dir, "aircraft_damage_dataset_v1")

# =========================
# 5) download .tar (daca nu exista deja)
# =========================
if not os.path.exists(tar_path):
    print(f"[info] descarc {tar_filename} in {base_dir} ...")
    urllib.request.urlretrieve(dataset_url, tar_path)
    print("[ok] descarcare terminata.")
else:
    print(f"[info] arhiva exista deja: {tar_path}")

# =========================
# 6) extrage .tar (sterge daca exista un folder vechi)
# =========================
if os.path.exists(extract_dir):
    print(f"[info] sterg folderul existent: {extract_dir}")
    shutil.rmtree(extract_dir)

print(f"[info] extrag in: {extract_dir}")
with tarfile.open(tar_path, "r") as tar:
    tar.extractall(path=extract_dir)
print("[ok] extragere completa.")

# =========================
# 7) verificare structura si cateva statistici
# =========================
def count_files(root):
    total = 0
    for _, _, files in os.walk(root):
        total += len(files)
    return total

total_files = count_files(extract_dir)
print(f"[info] total fisiere in {extract_dir}: {total_files:,}")

# subfoldere posibile
train_dir = os.path.join(extract_dir, "train")
val_dir   = os.path.join(extract_dir, "valid")  # uneori 'val' sau 'valid'
test_dir  = os.path.join(extract_dir, "test")

print("[info] posibile directoare:")
print("  train_dir:", train_dir, "  ->", "ok" if os.path.isdir(train_dir) else "nu exista")
print("  val_dir:  ", val_dir,   "  ->", "ok" if os.path.isdir(val_dir)   else "nu exista")
print("  test_dir: ", test_dir,  "  ->", "ok" if os.path.isdir(test_dir)  else "nu exista")

# =========================
# 8) pregatire generatoare pentru date
# =========================
train_datagen = ImageDataGenerator(rescale=1./255)
valid_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_rows, img_cols),   # redimensioneaza imaginile la dimensiunea ceruta de vgg16
    batch_size=batch_size,
    seed=seed_value,
    class_mode='binary',
    shuffle=True  # clasificare binara: dent vs crack
)
