from pathlib import Path
import shutil
import argparse


def copy_files(root : Path, dest : Path):
    try:
        for item in root.iterdir():
            if item.is_dir():
                copy_files(item,dest)
            else:
                ext = item.suffix[1:]
                if ext:
                    ext_d = dest / ext
                    ext_d.mkdir(parents=True, exist_ok=True)
                    shutil.copy(item, ext_d)
    except Exception as e:
        print(f"Error reading file: {e}")


if __name__ == "__main__":
    root = Path(input("Enter source folder "))
    dest = (input("Enter destination folder "))
    if not dest:
        dest = "dist"
    copy_files(root,Path(dest))
  

