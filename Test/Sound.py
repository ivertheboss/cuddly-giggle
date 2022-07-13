from gtts import gTTS
import Video


def makeSound(text, name):
    reddittext = text.replace("fuck", "duck")
    reddittext1 = reddittext.replace("dick", "pp")
    reddittext = reddittext1.replace("ass", "butt")
    tts = gTTS(reddittext, 'co.ck', "en")
    tts.save(name+'.wav')
