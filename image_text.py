import pytesseract
from PIL import Image
import pyttsx3

img = Image.open('quote.jpg')

pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
result = pytesseract.image_to_string(img)

with open('magic.txt',mode='w') as file:
    file.write(result)

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

speak(result)
