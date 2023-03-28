# Importing Essentials
from gtts import gTTS # for converting text to speech
from playsound import playsound # for Playing Converted Audio

def main():
	# Print Welcome Message.
	print("--------------------- Welcome to RoboSpeaker -----------------------")

	# Get Text as Input from the User.
	print("Please Enter the Text Which You Want this Programm to Play(Don't Include any Punctuation).")
	text = input(":- ")

	# Selecting Language in Which We want to convert the Audio.
	language = "en"


	# Specifying Speed, Text and Language of the Audio and Generating it.
	audio = gTTS(text=text, lang=language, slow=False, tld="com")

	# Saving the Audio as audio.mp3
	audio.save("audio.mp3")


	# Playing the Converted Audio
	playsound("audio.mp3")

if __name__ == "__main__":
	main()