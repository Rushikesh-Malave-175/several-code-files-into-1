import os

root_dir = r"C:\Assist\frontend\src"
output_file = r"C:\Assist\combined_output.txt"

with open(output_file, "w", encoding="utf-8") as out:
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    out.write(path + "\n")
                    out.write(f.read())
                    out.write("\n\n\n")
            except:
                pass