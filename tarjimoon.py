from googletrans import Translator

def tarjimon(matn):
    tarjima = Translator()
    til = tarjima.detect(matn).lang
    if til == "uz":
        return tarjima.translate(src="uz", dest="en", text=matn).text
    else:
        return tarjima.translate(dest="uz", text=matn).text