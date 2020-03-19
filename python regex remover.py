#!/usr/bin/env python3

import os, re, shutil

fileDirectory = "test/"
regex = re.compile(r'[0-9]+-[0-9a-f]{13}') #regex to match the files we're cleaning up

if __name__ == "__main__":
  os.chdir(fileDirectory)

  files = os.listdir(fileDirectory)
  files[:] = [i for i in files if regex.search(i)]
  for file in files:
    print("Removing file:",file)
    try:
      if (os.path.isdir(file)):
        shutil.rmtree(file)
      elif (os.path.isfile(file)):
        os.remove(file)
    except Exception as e:
      print("  Failed to remove file:",file,"due to error:",str(e))