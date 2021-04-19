import pyttsx3
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class Bibliography:
    Title = ""
    Author = ""
    Abstract = ""
    Journal = ""
    Year = ""
    def __init__(self):
        return

def str_clean(string):
    strclean = string.replace("=", " is ").replace("{", " ").replace("}", " ")
    strclean = strclean.replace("\t", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ")
    return strclean

# Get the input .bib file
Tk().withdraw()
filename = askopenfilename()

# Read the file and generate a list of bibliographies
f = open(filename, "r")
biblist = []
endoffile= False
bib = None
while not endoffile:
    try:
        line = f.readline()
    except UnicodeDecodeError:
        continue
    if (len(line)==0):
        endoffile=True
        continue
    if line.lstrip().startswith('@'):
        bib = Bibliography()
        biblist.append(bib)

    if line.lstrip().startswith("author"):
        authors = line.replace("author = ", "").replace(" and ", "  and  ")
        authlist = authors.split(" and ")
        newauthor = ""
        for auth in authlist:
            lastfirst = auth.split(',')
            firstlast = lastfirst[1] + lastfirst[0]
            firstlast = str_clean(firstlast)
            newauthor = newauthor + firstlast + ","
        bib.Author = "Author is " + newauthor
    elif line.lstrip().startswith("abstract"):
        bib.Abstract = "\t" + str_clean(line)
    elif line.lstrip().startswith("title"):
        bib.Title = "\t" + str_clean(line)
    elif line.lstrip().startswith("journal"):
        bib.Journal = "\t" + str_clean(line)
    elif line.lstrip().startswith("year"):
        bib.Year = "\t" + str_clean(line)
f.close()

# Generate a string to be read by the text to speech engine
textstring =""
for bib in biblist:
    textstring = textstring + bib.Author #+ "\n"
    textstring = textstring + bib.Year #+ "\n"
    textstring = textstring + bib.Title #+ "\n"
    textstring = textstring + bib.Journal #+ "\n"
    if (bib.Abstract == ""):
        textstring = textstring + "No abstract."
    else:
        textstring = textstring + bib.Abstract
    textstring += "Next. "


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice to something female
voices = engine.getProperty('voices')
voiceid = voices[0].id
for voice in voices:
    if (voice.id == "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"):
        voiceid = voice.id
        break
    if (voice.id == "com.apple.speech.synthesis.voice.tessa"): #we also like Samantha
        voiceid = voice.id
        break
engine.setProperty('voice', voiceid)

# Decreate the rate slightly
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)

# Get the output file
outputfile = asksaveasfilename(title = "Save to file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))

# Save the MP3 file, recording the time it took, and then report done!
starttime = time.time()
engine.save_to_file(textstring, outputfile)
engine.runAndWait()
print ("Done! It took %5.3f seconds" %(time.time() - starttime))
