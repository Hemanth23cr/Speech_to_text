#This program takes in audio and returns the audio as text

##Install pyadio
#pip install pyaudio

#Install the speech recognition package
#pip install SpeechRecognition

#Import the libraries
import speech_recognition as sr

#Record audio and return it as a string
def recordAudio():
  # Record Audio
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print('Say something!')
    audio = r.listen(source)

  # Speech recognition using Google Speech Recognition
  data = ""
  try:
      # Uses the default API key
      # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
      data = r.recognize_google(audio)
      print("You said: " + data)
  except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
  except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

  return data

recordAudio()