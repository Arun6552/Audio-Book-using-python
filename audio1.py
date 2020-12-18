import pyttsx3  #text-to-speech conversion library
import PyPDF2 # pure-python pdf library that we can use for splitting, merging, cropping, and transforming pages in our pdfs.
from tkinter.filedialog import *
import  time as t


# Initialize the Audio
audio = pyttsx3.init()

s=t.sleep(3)
# machine = pyttsx3.init()


file=askopenfilename()


# book = open('gita.pdf', 'rb') #Opens the file as read-only in binary format and starts reading from the beginning of the file.

Read_pdf = PyPDF2.PdfFileReader(file)
pages = Read_pdf.numPages
print("Total Number of pages in pdf  is",pages)





speed= audio.getProperty('rate')
print(speed)
rate1=audio.setProperty('rate', 150)




voice = audio.getProperty('voices')
# print(voices)

# changing index, changes voices, 0 for male
audio.setProperty('voice', voice[0].id)

#changing index, changes voices, 1 for female
audio.setProperty('voice', voice[1].id)


volume = audio.getProperty('volume')
print(volume)
volume=audio.setProperty('volume',1)



audio.say("Welcome the Audio Book ,....")

for num in range(7,pages):
    page = Read_pdf.getPage(num)
    text = page.extractText()
    print(text)
    audio.say(text)
    audio.runAndWait()
audio.stop()
audio.save_to_file(text, 'audio.mp3')
audio.runAndWait()