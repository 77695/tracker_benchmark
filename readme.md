# Trakcer Benchmark

This repository is modified from https://github.com/jwlim/tracker_benchmark. 

Goals:
- [x] **Light Weight**. Extra trackers and results are removed in this repository
- [ ] **No Bug**. Bugs are fixed.
- [ ] **Compatible**. Easy to use in python2 and python3

## Run new tracker
- Add script to running tracker in ```scripts/bscripts``` (see run_ExampleTracker.py)
- Import it in ```scripts/bscripts/__init__.py```

## Usage
Default (for all trackers, all sequences, all evaltypes(OPE, SRE, TRE))
- command : python run_trackers.py

For specific trackers, sequences, evaltypes    
- command : python run_trackers.py -t "tracker" -s "sequence" -e "evaltype"
- sequence can be name of Sequence, 'tb50', 'tb100' and 'cvpr13' (using data/tb_50.txt, tb_100.txt, cvpr13.txt)
- e.g.
    - python run_trackers.py -t IVT,TLD -s Couple,Crossing -e OPE,SRE)
    - python run_trackers.py -s tb50 

# Libraries
- matplotlib
- numpy
- Python Imaging Library (PIL)

# Troubleshooting
Segmentaion Fault when running 'python run_tracker.py ...' on MacOSX
- Set DYLD_LIBRARY_PATH environment variable.
- e.g.: export DYLD_LIBRARY_PATH=/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/Current/lib/:$DYLD_LIBRARY_PATH
