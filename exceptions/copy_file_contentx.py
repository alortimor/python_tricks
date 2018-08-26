#!/usr/bin/python3

"""
A typical try/except that will catch exceptions when doing file I/O:
  try:
    shutil.copy( str(source_file_path), str(target_file_path) )
  except FileNotFoundError:
    os.makedirs( str(target_file_path.parent) )
    shutil.copy( str(source_file_path), str(target_file_path) )
  except OSError as ex:
    print(ex)

The problem with the above try catch code is that the code executed within
the "except" may cause an exception, in which case the in-scope "try exept",
will not catch such an exception.
A way around this to nest another try except, as follows:

  try:
    shutil.copy( str(source_file_path), str(target_file_path) )
  except FileNotFoundError:
    try:
      os.makedirs( str(target_file_path.parent) )
      shutil.copy( str(source_file_path), str(target_file_path) )
    except OSError as ex:
      print(ex)
  except OSError as ex:
    print(ex)
"""
print (__doc__)

from pathlib import Path
import shutil
import os
source_path = Path(os.path.expanduser('~/bin'))
target_path = Path(os.path.expanduser('~/sample_code/python/sh'))

print("Source path ", source_path)
print("Target path ", target_path)

for source_file_path in source_path.glob('*.sh'):
  source_file_detail = source_file_path.relative_to(source_path)
  target_file_path = target_path / source_file_detail
  try:
    shutil.copy( str(source_file_path), str(target_file_path) )
  except FileNotFoundError:
    os.makedirs( str(target_file_path.parent) )
    shutil.copy( str(source_file_path), str(target_file_path) )
  except OSError as ex:
    print(ex)

