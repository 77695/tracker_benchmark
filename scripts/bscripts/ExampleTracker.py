import time
import os
import numpy as np
from ..config import *

def run(seq, rp, bSaveImage):
    x = seq.init_rect[0] - 1
    y = seq.init_rect[1] - 1
    w = seq.init_rect[2]
    h = seq.init_rect[3]

    command = list(map(str,['python run_tracker.py', seq.name, seq.path, seq.startFrame, seq.endFrame, 
        seq.nz, seq.ext, x, y, w, h]))

    tic = time.clock()
    os.system(' '.join(command))
    duration = time.clock() - tic

    result = dict()
    res = np.loadtxt('{0}_BSBT.txt'.format(seq.name), dtype=int)
    result['res'] = res.tolist()
    result['type'] = 'rect'
    result['fps'] = round(seq.len / duration, 3)

    return result