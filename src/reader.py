import pyttsx3

class Reader:
    def __init__(self):
        self.engine = pyttsx3.init()
    
    def set_rate(self, rate = 150):
        """
        Velocità di lettura, no args = default
        rate: int
            = 150 ~ lettura normale ca.
            = 125 ~ flemma
        """
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume = 1.0):
        """
        Volume della voce che legge, no args = default
        volume: float
            = 1.0 ~ 100% dell'attuale volume di os
        """
        self.engine.setProperty('volume', volume)
    
    def set_voice(self, lang, sex):
        alowed_lang = ['it', 'en', 'fr']
        if lang in alowed_lang:
            voices = self.engine.getProperty('voices')
            if lang == 'it':
                if sex == 'm':
                    self.engine.setProperty('voice', voices[21].id)
                else:
                    self.engine.setProperty('voice', voices[1].id)
            elif lang == 'en':
                if sex == 'm':
                    self.engine.setProperty('voice', voices[0].id)
                else:
                    self.engine.setProperty('voice', voices[33].id)
            if lang == 'fr':
                print("French : MALE ONLY SRY 🥲")
                self.engine.setProperty('voice', voices[38].id)
    
    def debug_list_lang(self):
        i = 0
        for prop in self.engine.getProperty('voices'):
            print(f"{i} : {prop.languages}\n{prop}")
            i += 1



if __name__ == "__main__":
    r = Reader()
    r.debug_list_lang()

    test_phrases = [
        ('Hello', 'en'),
        ('Ciao, messaggio di prova per le email. A presto', 'it'),
        ('Halo', 'fr')
    ]

    r.set_volume()
    r.set_rate()
    for test in test_phrases:
        print(test[1 ])
        r.set_voice(test[1], 'm')
        r.engine.say(test[0])
        r.engine.runAndWait()
        r.engine.stop()
        r.set_voice(test[1], 'f')
        r.engine.say(test[0])
        r.engine.runAndWait()
        r.engine.stop()
