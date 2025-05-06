# ipynb-code-extractor

A simple command-line utility to extract all Python code cells from a single Jupyter notebook (`.ipynb`) and output them as a `.py` script or print to standard output.

## Features

* Reads a single Jupyter notebook file
* Extracts every code cell in order
* Prepends a header comment with the source notebook name
* Outputs combined code to stdout or writes to a specified `.py` file

## Requirements

* Python 3.6 or higher

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/vigneshv1cky/ipynb-code-extractor.git
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

## Usage

```bash
# Print extracted code from notebook.ipynb to the terminal
./extract_code.py path/to/notebook.ipynb

# Write extracted code to a Python file
./extract_code.py path/to/notebook.ipynb --out output_script.py
```

### Arguments

* `notebook` (positional): Path to the `.ipynb` file to process.
* `-o, --out` (optional): Path to write the resulting `.py` file. If omitted, the code is printed to stdout.

### Example

```bash
# Extract code from analysis.ipynb into analysis.py
./extract_code.py analysis.ipynb -o analysis.py
```

## Contributing

Contributions and improvements are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
