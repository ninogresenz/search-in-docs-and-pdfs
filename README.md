# Search in DOCs and PDFs

## Prerequisites
* Python 3
* pip
* some libs listed ins install.sh

## Installation
```bash
./install.sh
pip install -r requirements.txt
```

## Usage
### help
```bash
$ ./search.py
Usage:
main.py [options] [regex expression] [path]

Options: # not yet suppored
  -r --recursive         search recursively through all folders

Supported files formats:
  PDF   yes
  XLS   not yet
  XLSX  not yet
```

### Search a string
```bash
./search.py "Interesting" ~/Documents
  Matches  File
        3  /home/username/Documents/1.pdf
        7  /home/username/Documents/2.pdf
```