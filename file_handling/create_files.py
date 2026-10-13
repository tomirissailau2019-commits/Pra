try:
    with open("new_file.txt", "x") as f:
        f.write("Newly created file.")
except FileExistsError:
    print("File already exists!")