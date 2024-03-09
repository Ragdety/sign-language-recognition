import os
import logging

from gtts import gTTS 
from playsound import playsound

logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s: %(message)s')


class SLAudio:
  def __init__(self, text, lang='en', log_level=logging.INFO):
    """
    Initialize the SLAudio object with the text and language

    :param text: The text that you want to convert to audio
    :param language: Language in which you want to convert, defaults to 'en'
    :param log_level: The log level, defaults to logging.INFO
    """
    self.text = text
    self.lang = lang
    self.log_level = log_level

    self.logger = logging.getLogger(__name__)
    self.gTTS = gTTS(text=self.text, lang=self.lang, slow=False)
    self.file = None

  def save(self, filename):
    """
    Save the audio to a file

    :param filename: The name of the file
    """
    self.logger.debug(f"Saving the audio to {filename}")
    self.gTTS.save(filename)
    self.logger.info(f"Saved audio to {filename}")

    self.file = filename
      
  def play(self):
    """
    Play the audio
    """
    playsound(self.file)
    self.logger.info(f"Played audio from {self.file}")
