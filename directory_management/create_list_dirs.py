from pathlib import Path
import os

root = Path("practice_data")
nested = root / "texts" / "examples"

# Create nested directories
nested.mkdir(parents=True, exist_ok=True)
(root / "texts" / "example.txt").write_text("Example file\n", encoding="utf-8")
(nested / "notes.txt").write_text("Nested example\n", encoding="utf-8")

# List directories only, files only, and all items in a path
target = root
print("Current working directory:", os.getcwd())
print("All items:", [item.name for item in target.iterdir()])
print("Directories only:", [item.name for item in target.iterdir() if item.is_dir()])
print("Files only:", [item.name for item in target.iterdir() if item.is_file()])

# Find files by extension, including nested directories
print(".txt files:")
for item in target.rglob("*.txt"):
    print(item)

# Demonstrate os.listdir()
print("os.listdir():", os.listdir(target))

# os.mkdir() creates one directory level; os.makedirs() creates nested levels
os.mkdir("single_directory") if not Path("single_directory").exists() else None
os.makedirs("parent_directory/child_directory", exist_ok=True)

# os.chdir() changes the working directory; use carefully
# os.chdir(root)  # Uncomment to change to the practice_data directory.

# os.rmdir() removes only an empty directory
empty_dir = Path("empty_directory")
empty_dir.mkdir(exist_ok=True)
empty_dir.rmdir()
s