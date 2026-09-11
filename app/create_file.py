from datetime import datetime
import os
import sys


def main() -> None:
    directories = []
    file_name = None

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            i += 1
            while i < len(sys.argv) and not sys.argv[i].startswith("-"):
                directories.append(sys.argv[i])
                i += 1
            continue
        if sys.argv[i] == "-f":
            i += 1
            if i < len(sys.argv) and not sys.argv[i].startswith("-"):
                file_name = sys.argv[i]
                i += 1
            continue
        i += 1

    dir_path = ""
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)

    if file_name is not None:
        if dir_path:
            full_path = os.path.join(dir_path, file_name)
        else:
            full_path = file_name

        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_content = [timestamp]
        for index, line in enumerate(lines, start=1):
            new_content.append(f"{index} {line}")
        block = "\n".join(new_content)

        file_exists = (
            os.path.exists(full_path)
            and os.path.getsize(full_path) > 0
        )
        mode = "a" if file_exists else "w"

        with open(full_path, mode, encoding="utf-8") as f:
            if file_exists:
                f.write("\n\n" + block)
            else:
                f.write(block)


if __name__ == "__main__":
    main()
