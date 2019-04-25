# img2txt
Program to convert image to text file using pytesseract.
Pytesseract is a python wrapper for Google Tesseract.

### Dependency
You will need Python3.x and [Google Tesseract](https://opensource.google.com/projects/tesseract) to run this program.he packages are listed below:

To install [Google Tesseract](https://opensource.google.com/projects/tesseract) in Mac OS, run below commands in terminal:
```sh
$ brew install tesseract
$ brew install tesseract-lang
```

Requirements for python virtual environment:
- Pillow==6.0.0
- pytesseract==0.2.6

### How to convert
Put all images in 'images' directory and run text_extract.py. It will convert and create text files in 'text' directory.