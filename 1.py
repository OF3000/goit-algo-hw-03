from pathlib import Path
import shutil


def copy_files(root : Path, dist : Path = Path("dist")):
    try:
        for item in root.iterdir():
            if item.is_dir():
                copy_files(item,dist)
            else:
                ext = item.suffix[1:]
                if ext:
                    ext_d = dist / ext
                    ext_d.mkdir(parents=True, exist_ok=True)
                    shutil.copy(item, ext_d)
    except Exception as e:
        print(f"Error reading file: {e}")


if __name__ == "__main__":
    root = Path("/Users/fo/Repo/goit-algo-hw-03/")
    copy_files(root,root / Path("Dir"))
    #copy_files(root)
