import os

# clears the directory and all subdirectories of all json files
def clearDirectory(path, prev_path):
    os.chdir(path)
    for file in os.listdir():
        if file.endswith(".json"):
            os.remove(file)
        elif os.path.isdir(file):
            clearDirectory(file, os.getcwd())
            # check if directory is empty and delete it, if it is
            if not os.listdir(file):
                os.rmdir(file)
    os.chdir(prev_path)

def main():
  curr_path = os.getcwd()
  for file in os.listdir():
      if file.endswith(".json"):
          os.remove(file)
      elif os.path.isdir(file):
          clearDirectory(file, curr_path)

if __name__ == "__main__":
    main()
