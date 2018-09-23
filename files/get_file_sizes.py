#!/home/bluefrog/anaconda3/bin/python3
import pathlib

file_sizes = []
print("Present working directory : {}/n".format(pathlib.Path.cwd()))
rootdir = pathlib.Path("/home/bluefrog/sample_code/python")
for python_file in rootdir.glob("**/*.py"):
    fs = python_file.stat().st_size
    file_sizes.append(fs)
    print(python_file, fs)

print("Number of files : {} ".format(len(file_sizes)))
print("Average file size {}".format(round(sum(file_sizes)/len(file_sizes),2)))
