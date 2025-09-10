import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Load the audio file
audio_file_path = r'C:\Users\User\Desktop\podcasts\download (4).wav'  # Make sure you have a 'sample.wav' file in the same directory

try:
    with sr.AudioFile(r'C:\Users\User\Desktop\podcasts\download (10).wav') as source:
        print("Processing audio...")
        audio_data = r.record(source)  # Read the entire audio file

    # Perform speech recognition using Google Web Speech API
    text = r.recognize_google(audio_data)
    print("Transcription:", text)

except sr.UnknownValueError:
    print("Speech Recognition could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except FileNotFoundError:
    print(f"Error: Audio file not found at '{audio_file_path}'.")