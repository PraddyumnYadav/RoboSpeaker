from django.shortcuts import render
from django.http import FileResponse
from gtts import gTTS
import os

def convert_text(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        language = "en"
        audio = gTTS(text=text, lang=language, slow=False)
        audio_file = f"robospeaker_app/static/audio/{text[:10]}.mp3"
        audio.save(audio_file)
        return FileResponse(open(audio_file, 'rb'))
    else:
        return render(request, 'index.html')
from django.shortcuts import render

# Create your views here.
