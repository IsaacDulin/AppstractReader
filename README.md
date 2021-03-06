# AppstractReader
Program to read bibliography files into mp3, v1.0


# Setup
This program should work on Mac and Windows. We are still working on Ubuntu/Linux compatibility.

First, install pyttsx3 using pip or other preferred methods to install python packages.
```
pip install pyttsx3
```
If you are using Python 2.x, you may need to install Tk:
```
pip install tkinter
```

# Usage
Run AppstractReader.py on your terminal:
```
python AppstractReader.py
```
You will be prompted for an input file (.bib) and a target save file (.mp3). The contents of the
bibliography will be parsed and read to the .mp3 file. The file will read the title, author(s), 
journal, year, and abstract (if available) of each entry in the .bib file. 

Once you have the .mp3 file, you can load it onto iTunes or any other song player. You can also load it onto a Garmin or another smart watch that supports .mp3.



# Authors
Isaac Dulin: E-mail isaacdulin [at] gmail.com

Stephanie Kestelman: E-mail skestelman [at] g.harvard.edu.


AppstractReader is licensed under the MIT License.
