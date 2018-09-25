import os
import importlib
for fn in os.listdir(os.path.dirname(__file__)):
    if fn == '__init__.py' or os.path.splitext(fn)[1] != '.py':
        continue
    trk_name = fn.replace('.py', '')
    importlib.import_module('scripts.bscripts.{}'.format(trk_name))