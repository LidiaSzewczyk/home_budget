import os


def save_env(key, val):
    file_path = os.path.join(".ENV")
    with open(file_path, "r") as file:
        data = file.readlines()

    new_data = []

    for line in data:
        if key == line.split(':')[0]:
            new_data.append(f"{key}: {val}\n")
        else:
            new_data.append(line)

    with open(file_path, "w") as file:
        file.writelines(new_data)


