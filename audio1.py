import pyttsx3  # text-to-speech conversion library
import PyPDF2  # pure-python pdf library that we can use for splitting, merging, cropping, and transforming pages in our pdfs.
from tkinter.filedialog import *

# Initialize the Audio
audio = pyttsx3.init()

audio.say("Welcome the Audio Book ")
audio.say("Please Select the PDF")
audio.runAndWait()

# runAndWait() → None
# Blocks while processing all currently queued commands. Invokes callbacks for engine notifications appropriately.
# Returns when all commands queued before this call are emptied from the queue.

file = askopenfilename()  # Opens the file as read-only in binary format and starts reading from the beginning of the file.
# book = open('gita.pdf', 'rb')
file_name=file.split('.')[1]

if(file_name!='pdf'):
    audio.say("You have not selected Pdf File. Please Select the PDF file Only")
    audio.runAndWait()


else:
    # Read the pages
    Read_pdf = PyPDF2.PdfFileReader(file)
    pages = Read_pdf.numPages
    print("\nTotal Number of pages in pdf  is", pages)


    ##Speed  of the Audio

    speed = audio.getProperty('rate')
    print("\nThe Current Speed is", speed)
    audio.say("The Current Speed is 200")
    audio.say('Do You want to change the Speed of the audio Enter 1 for Yes and 0 for No')
    audio.runAndWait()

    spd = int(input("\nDo You want to change the Speed of the audio ?\nEnter 1 for Yes and 0 for No : "))
    if (spd == 1):
        audio.say('Enter 100 for 1x,125 for 1.25x,150 for 1.5x ,175 for 1.75x ,200 for 2x speed :')
        audio.runAndWait()
        spd_user = int(input("\nEnter 100 for 1x,125 for 1.25x,150 for 1.5x ,175 for 1.75x ,200 for 2x speed :"))
        audio.setProperty('rate', spd_user)


    ##Voice of the Audio

    voice = audio.getProperty('voices')
    audio.say('This is My Voice')
    audio.say('Do You want to change My Voice ? Enter 1 for Yes and 0 for No :')
    audio.runAndWait()

    vce = int(input("\nDo You want to change the Voice of the audio ?\nEnter 1 for Yes and 0 for No :"))
    if (vce == 1):
        audio.say('Enter 0 for Male Voice and 1 for female Voice')
        audio.runAndWait()
        vce_user = int(input("Enter 0 for Male Voice and 1 for female Voice :"))
        audio.setProperty('voice', voice[vce_user].id)

    # Volume of the Audio

    volume = audio.getProperty('volume')
    print("\nThe  Current volume is ", volume)
    audio.say("The current Volume is 1")
    audio.say('Do You want to change the Volume of the audio Enter 1 for Yes and 0 for No :')
    audio.runAndWait()

    vlm = int(input("\nDo You want to change the Speed of the audio ?\nEnter 1 for Yes and 0 for No :"))
    if (vlm == 1):
        audio.say('Enter The volume ranges from 0 to 1, where 0 is the minimum volume and 1 being the maximum volume')
        audio.runAndWait()
        vlm_user = float(input("\nEnter The volume ranges from 0 to 1, where 0 is the min volume and 1 being the max volume :"))
        speed = audio.setProperty('volume', vlm_user)

    for num in range(3, 4):
        page = Read_pdf.getPage(num)
        text = page.extractText()
        print("\nI am going to read this:\n")
        audio.say("I am going to read this ")
        print(text)
        audio.say(text)
        audio.runAndWait()
    audio.stop()
    audio.save_to_file(text, 'audio.mp3')
    audio.runAndWait()


