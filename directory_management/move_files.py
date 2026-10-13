from pathlib import Path
import shutil

base = Path("file_transfer_demo")
source_dir = base / "source"
destination_dir = base / "destination"
source_dir.mkdir(parents=True, exist_ok=True)
destination_dir.mkdir(parents=True, exist_ok=True)

source_file = source_dir / "hello.txt"
source_file.write_text("Hello from the source folder!\n", encoding="utf-8")

# Copy a file between directories
copied_file = destination_dir / source_file.name
shutil.copy2(source_file, copied_file)
print("Copied to:", copied_file)

# Move a file between directories
moving_file = source_dir / "move_me.txt"
moving_file.write_text("This file will be moved.\n", encoding="utf-8")
moved_file = destination_dir / moving_file.name
shutil.move(str(moving_file), str(moved_file))
print("Moved to:", moved_file)
