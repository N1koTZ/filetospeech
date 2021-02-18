
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os

  
# The text file that you want to convert to audio 
 
file = open("40k.txt", "r").read().replace("\n", " ")
# Language in which you want to convert 
language = 'en'


# Passing the text and language to the engine,  

myobj = gTTS(text=str(file), lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("40ksoundtestsmall.mp3") 
  
# Playing the converted file 
os.system("40ksoundtestsmall.mp3") 
