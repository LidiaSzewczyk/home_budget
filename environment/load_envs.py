import os


def load_envs():
    file_path = os.path.join(".ENV")
    os.environ['ROOT_DIR'] = os.path.abspath(".")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                arr = line.replace("\n", "").split(': ')
                # print(arr)
                os.environ[arr[0]] = arr[1]
    else:
        print("Wrong configuration: check environment variables")
