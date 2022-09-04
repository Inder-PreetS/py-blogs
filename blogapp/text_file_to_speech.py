from gtts import gTTS 
import os
import shutil 

def text_to_audio(text_file, blogname):
    text_file =text_file
    language = 'en'

    output = gTTS(text=text_file, lang=language, slow=False)
     
    filename = str(blogname)+".mp3"
    output.save(filename)
    shutil.move(os.path.join(filename), os.path.join("./media", filename))
    return filename
