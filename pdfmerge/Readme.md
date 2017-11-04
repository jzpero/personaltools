# pdfmerge
## Description
A basic pdf merging tool in Python.

## Usage
Example:

```
python pdfmerge.py file1.pdf file2.pdf [0:10:2] [1:5] -o file3.pdf
```

Planned options:
```
usage: pdfmerge.py [-h] [-r RANGES [RANGES ...]] [-a] [-o OUTFILENAME]
                   filenames [filenames ...]

Merges PDFs together.

positional arguments:
  filenames             PDF files to merge together.

optional arguments:
  -h, --help            show this help message and exit
  -r RANGES [RANGES ...]
                        Ranges (Python slicing notation)
  -a
  -o OUTFILENAME        output filename
```

## Dependencies
- [PyPDF2](https://github.com/mstamy2/PyPDF2)

## To-Do
- [ ] implement alternate flag
- [ ] fix bookmark merging
