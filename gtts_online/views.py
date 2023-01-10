from io import BytesIO
from gtts import gTTS
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@cache_page(60 * 60 * 24 * 5) # 5 days
def get_sound(request):
    text = request.GET.get('text')
    tl = request.GET.get('tl')
    if not text or not tl:
        return HttpResponse(
            "<html><body>"
            "Please specify 'tl' and 'text' params"
            "</body></html>", 
            status=400
        )
    mp3_fp = BytesIO()
    try:
        tts = gTTS(text, lang=tl)
    except ValueError as e:
        return HttpResponse(
            "<html><body>%s</body></html>" % str(e), status=400
        )
    tts.write_to_fp(mp3_fp)
    return HttpResponse(mp3_fp.getbuffer(), content_type='audio/mpeg')

