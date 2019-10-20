import os
import librosa
import numpy as np
import time

import warnings
warnings.filterwarnings('ignore')

def get_all_files(path_name):
    tmp = os.walk(path_name)
    mp4 = []
    for address, dirs, files in tmp:
        for file in files:
            mp4.append(address + '/' + file)
    return mp4


start_time = time.time()
file = get_all_files('audio')
for item in file:
   y, sr = librosa.core.load(item)
   mfcc = librosa.feature.mfcc(y=y, sr=sr)
   i = item.rfind('/')
   if os.path.exists('1' + item[:i]) == False:
       os.makedirs('1' + item[:i])
   np.save('1' + item[:len(item) - 3] + 'npy', mfcc)

print("i finish my fork in %s seconds" % (time.time() - start_time))

