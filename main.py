from pypdf import PdfReader
import pyttsx3



reader = PdfReader('Dummy.pdf')                #Read PDF file

speaker=pyttsx3.init()
voices= speaker.getProperty('voices')         #Change voice to female
speaker.setProperty('voice',voices[1].id)
for n in range(0,len(reader.pages)):           #Change when need to start reading from specific page
    page = reader.pages[n]
    text = page.extract_text()
    t=speaker.say(text)
    print(text) 
    speaker.runAndWait()
