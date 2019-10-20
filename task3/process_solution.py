import os
import librosa
import numpy as np
import time
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor
import warnings
warnings.filterwarnings('ignore')

def get_all_files(path_name):
    tmp = os.walk(path_name)
    mp4 = []
    for address, dirs, files in tmp:
        for file in files:
            mp4.append(address + '/' + file)
    return mp4

def make_mfcc(item):
    y, sr = librosa.core.load(item)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    i = item.rfind('/')
    if os.path.exists('2' + item[:i]) == False:
        os.makedirs('2' + item[:i])
    np.save('2' + item[:len(item) - 3] + 'npy', mfcc)
    return 0


start_time = time.time()
file = get_all_files('audio')
with ProcessPoolExecutor(max_workers=2) as pool:
    for item in file:
        pool.submit(make_mfcc, item)

print("i finish my fork in %s seconds" % (time.time() - start_time))
