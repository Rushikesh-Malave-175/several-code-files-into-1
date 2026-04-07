import os

root_dir = r"C:\Users\rushi\Downloads\goykar\Goykar-Assist"
output_file = r"C:\Users\rushi\Downloads\goykar\Goykar-Assist.txt"

allowed_ext = (
    ".js", ".jsx", ".ts", ".tsx", ".json", ".html", ".css", ".scss",
    ".py",
    ".java", ".kt", ".kts", ".groovy",
    ".c", ".cpp", ".h", ".hpp",
    ".cs",
    ".go",
    ".rs",
    ".php",
    ".rb",
    ".swift",
    ".sh", ".bash", ".zsh", ".ps1",
    ".yaml", ".yml", ".toml", ".xml", ".ini", ".env",
    ".sql",
    ".md", ".txt"
)

skip_dirs = {
    "node_modules", ".git", "dist", "build",
    "__pycache__", ".next", "out", "venv", ".venv"
}

skip_files = {
    "package-lock.json",
    ".env",
    "package.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "bun.lockb"
}

with open(output_file, "w", encoding="utf-8") as out:
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in skip_dirs]

        for file in files:
            path = os.path.join(root, file)

            if path == output_file:
                continue

            if file in skip_files:
                continue

            if ".min." in file:
                continue

            if not file.lower().endswith(allowed_ext):
                continue

            try:
                if os.path.getsize(path) > 200_000:
                    continue

                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    out.write(f"\n===== {path} =====\n")
                    for line in f:
                        out.write(line)
                    out.write("\n\n")
            except Exception as e:
                print(f"Skipped {path}: {e}")