from django.shortcuts import render
from django.http import FileResponse
from gtts import gTTS
import os

def convert_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        language = "en"
        audio = gTTS(text=text, lang=language, slow=False)
        audio_file = os.path.join('robospeaker_app', 'static', 'audio', 'audio.mp3')
        audio.save(audio_file)
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
