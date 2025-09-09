import speech_recognition as sr

class STTHelper:
    def __init__(self):
        self._r = sr.Recognizer()

    @staticmethod
    def write_bytes_to_wav(path, data_bytes):
        with open(path, 'wb') as f:
            f.write(data_bytes)


    def text_from_speach(self, _id, data_bytes) -> str:
        path = _id+'.wav'
        self.write_bytes_to_wav(path, data_bytes)
        with sr.AudioFile(path) as source:
            audio_data = self._r.record(source)  # Read the entire audio file

        # Perform speech recognition using Google Web Speech API
        text = self._r.recognize_google(audio_data)
        return text




