#!/usr/bin/python3

from pathlib import Path
import shutil
import os
source_path = Path(os.getcwd() + '/source_path')
target_path = Path(os.getcwd() + '/target_path')

for rst_file in source_path.glob('*.rst'):
    shutil.copy( str(source_path + '/' + rst_file), str(target_path + '/' + rst_file))
