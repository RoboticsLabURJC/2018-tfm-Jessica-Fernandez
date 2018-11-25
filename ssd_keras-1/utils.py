
import numpy as np
import os
from keras.preprocessing import image
from PIL import Image

def normalize_input(x):
    return (x - 127.5) / 127.5

def denormalize_output(x):
    return (x * 127.5) + 127.5

def make_paths_from_directory(root):
    input_paths = []
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'rb') as fp:
                magic = fp.read(8)

            if magic.startswith(b'GIF89a') or magic.startswith(b'GIF87a'):
                filetype = 'gif'
            elif magic == b'\xff\xd8\xff\xe0\x00\x10JF':
                filetype = 'jpeg'
            elif magic.startswith(b'\x89PNG'):
                filetype = 'png'
            else:
                print(' unsupported file type', repr(magic), filepath)
                continue
            input_paths.append(filepath)
    return input_paths

def make_arrays_from_paths(paths, preprocess=None, target_size=None):
    rv = []
    for path in paths:
        img = image.load_img(path, target_size=target_size)
        ar = image.img_to_array(img)
        if preprocess:
            ar = preprocess(ar)
        rv.append(ar)
    return np.array(rv)

def generate_reconst_img(path, model, x):
    out = model.predict_on_batch(x)
    out = denormalize_output(out).astype(np.uint8)
    out = np.concatenate(out,axis=0)
    x = denormalize_output(x).astype(np.uint8)
    x = np.concatenate(x,axis=0)
    final = np.concatenate((x,out),axis=1)
    final = Image.fromarray(final)
    final.save(path)
