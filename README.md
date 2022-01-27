# AlexaPythonProject
Made use of python programming language to make a virtual assistant named Alexa.

Started out by installing the necessary packages required to fulfill this project. The packages include

1. pyttsx3
2. pyaudio
3. SpeechRecogniton
4. pywhatkit
5. webbrowser
6. wikipedia
7. datetime

When we press on the run button, about after 2 seconds we see a prompt _listening..._ in the terminal window asking us to say something. We then say suppose 
ask ' _alexa open youtube_', here the webbrowser package comes in handy and opens youtube.com in a new tab in our web browser. In case a sentence is incomprehensible to alexa it simply return a verbal message as '_Sorry please try again later._'

Coming to the part where we need to get some information we make use of wikipedia package that gives a short info about our query. The question can be asked in multiple types like '_what is , who is a/an , what is a/an, tell me about._'
