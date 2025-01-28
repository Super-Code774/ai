from gtts import gTTS
import playsound

def text_to_speech(text, lang='en'):
    # Create a gTTS object with the text and language
    tts = gTTS(text=text, lang=lang)
    
    # Save the audio file
    audio_file = "output.mp3"
    tts.save(audio_file)
    
    # Play the audio file
    playsound.playsound(audio_file)

# Example usage
text = "Hello, how are you?"
text_to_speech(text)
