
# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os
import shutil 

def text_to_audio (text_file, blogname):
    text_file =text_file
    fh = open(text_file, "r")
    myText = fh.read().replace("\n", " ")

    # Language we want to use 
    language = 'en'

    output = gTTS(text=myText, lang=language, slow=False)
     
    filename = str(blogname)+".mp3"
    v=output.save(filename)
    fh.close()
    os.system("start"+filename)

    shutil.move(os.path.join(filename), os.path.join("D:/audioscript/audiofiles", filename))
    # shutil.move(filename, "D:/audioscript/audiofiles")


d = "D:/audioscript/test.txt"
blog="sahil"

text_to_audio(d,blog)