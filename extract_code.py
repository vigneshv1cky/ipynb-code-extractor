#!/usr/bin/env python3
import json
import argparse
import sys
from pathlib import Path


def extract_code_from_notebook(nb_path):
    """
    Load a .ipynb file and return a list of its code-cell sources.
    """
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    code_cells = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            # cell['source'] may be either a string or list of strings
            src = cell.get("source")
            if isinstance(src, list):
                src = "".join(src)
            code_cells.append(src.rstrip())
    return code_cells


def main():
    parser = argparse.ArgumentParser(
        description="Extract code cells from a single Jupyter notebook"
    )
    parser.add_argument("notebook", help="Path to a single .ipynb file")
    parser.add_argument(
        "--out", "-o", help="Optional output .py file; if omitted, prints to stdout"
    )
    args = parser.parse_args()

    path = Path(args.notebook)
    if not path.exists() or path.suffix != ".ipynb":
        print(
            f"Error: {args.notebook} not found or not a .ipynb file",
            file=sys.stderr,
        )
        sys.exit(1)

    code_cells = extract_code_from_notebook(path)
    header = f"# --- Code from `{path.name}` ---\n"
    output = header + "\n\n".join(code_cells) + "\n"

    if args.out:
        out_path = Path(args.out)
        out_path.write_text(output, encoding="utf-8")
        print(f"Wrote code from {path.name} → {out_path}")
    else:
        print(output)


if __name__ == "__main__":
    main()
