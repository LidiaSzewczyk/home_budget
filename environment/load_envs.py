import os


def find_project_root():
    return os.path.join(os.path.dirname(__file__), '..')


def load_envs():
    project_root = find_project_root()

    os.environ['ROOT_DIR'] = project_root
    file_path = os.path.join(project_root, ".ENV")

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                arr = line.replace("\n", "").split(': ')
                os.environ[arr[0]] = arr[1]
    else:
        print("Wrong configuration: check environment variables.")
