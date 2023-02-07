'''This is a simple implementation that uses the Google Speech 
Recognition API. There are other APIs available as well, 
and you can also use the libraries for transcribing 
audio files stored on the disk.'''


import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
try:
    # using google speech recognition
    print("Text: "+r.recognize_google(audio_text))
except:
     print("Sorry, I did not get that")
