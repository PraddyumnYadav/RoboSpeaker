# Importing Essentials
import time  # for using time.sleep()
from gtts import gTTS  # for converting text to speech
import pygame  # for playing the converted audio
import soundfile as sf  # for getting the length of the audio


# Creating Main Program
def main():
    # Print Welcome Message.
    print("--------------------- Welcome to RoboSpeaker -----------------------")
    print("Please Enter the Text Which You Want this Program to Play (Don't Include any Punctuation).")
    print("Press 'q' to quit.")

    while True:
        # Get Text as Input from the User.
        text = input(":- ")

        # Selecting Language in Which We want to convert the Audio.
        language = "en"

        # Exit the Program if input is q
        if text == "q":
            break

        # Run Speak Function with Error Handling
        try:
            speak(text, language)
        except Exception as e:
            print("An error occurred while processing your request:", e)
            continue


# Creating speak Function
def speak(text, language):
    # Convert text to speech using gTTS
    audio = gTTS(text=text, lang=language, slow=False)

    # Save the audio to a file
    audio_file = "audio.mp3"
    audio.save(audio_file)

    # Initialize pygame
    pygame.init()

    # Load the audio file and play it
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Stop Time for Audio Length
    time.sleep(get_audio_length(audio_file))

    # stop the music
    pygame.mixer.music.stop()

    # Quit pygame
    pygame.quit()


# Create a Function for Checking Length of Audio
def get_audio_length(filename):
    with sf.SoundFile(filename) as f:
        return len(f) / f.samplerate


# Run the main Function
main()
