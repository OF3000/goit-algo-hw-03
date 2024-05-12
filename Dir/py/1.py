from pathlib import Path
import shutil

# ANSI escape codes for colored output
COLOR_BLUE = ""
COLOR_RESET = ""

def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    if path.is_dir():
        # Use blue color for directories
        print(indent + prefix + COLOR_BLUE + str(path.name) + COLOR_RESET)
        indent += "    " if prefix else ""

        # Get a sorted list of children, with directories last
        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            # Check if the current child is the last one in the directory
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + str(path.name))


def copy_files(root : Path,dist : Path = "dist"):
    try:
        for item in root.iterdir():
            if item.is_dir():
                copy_files(item,dist)
            else:
                ext = item.suffix[1:]
                if ext:
                    print(ext)
                    ext_d = dist / ext
                    ext_d.mkdir(parents=True, exist_ok=True)
                    shutil.copy(item, ext_d)
    except Exception as e:
        print(f"Error reading file: {e}")


if __name__ == "__main__":
    root = Path("/Users/fo/Repo/goit-algo-hw-03/")
    #display_tree(root)
    copy_files(root,root / Path("Dir"))
    copy_files(root)
