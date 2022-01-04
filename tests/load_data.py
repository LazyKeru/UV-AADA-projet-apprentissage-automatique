
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import project.function as pf

data_path = '../dataset'

data = pf.load_data(data_path)
