from SLAudio import SLAudio

# The text that you want to convert to audio 
mytext = 'test audio'
# Language in which you want to convert 
language = 'en'

sl_audio = SLAudio(text=mytext) 
sl_audio.save("test.mp3") 
  
sl_audio.play()