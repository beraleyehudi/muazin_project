from app.connections import MongoConnection
from app.dal import MongoDal
import pymongo
import speech_recognition as sr

def get_all_documents(collection):
    """List all tweets in the database."""
    return list(collection.find())

def from_bytes_to_audio(file_name, data_bytes):
    with open(file_name, 'wb') as f:
        f.write(data_bytes)

dal = MongoDal(MongoConnection())
client = pymongo.MongoClient("mongodb://localhost:27017/")
data_base = client["muazin"]
coll = data_base['audio']

all_document = get_all_documents(coll)
# print(all_document)
print(type(all_document))
print(len(all_document))

audio_data = all_document[-1]['data']
print(type(audio_data))

audio_file_name = 'somting.wav' # Make sure you have a 'sample.wav' file in the same directory
from_bytes_to_audio(audio_file_name, audio_data)



r = sr.Recognizer()

# Load the audio file

try:
    with sr.AudioFile(audio_file_name) as source:
        print("Processing audio...")
        audio_data = r.record(source)  # Read the entire audio file

    #Perform speech recognition using Google Web Speech API
    text = r.recognize_google(audio_data)
    print("Transcription:", text)

except sr.UnknownValueError:
    print("Speech Recognition could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except FileNotFoundError:
    print(f"Error: Audio file not found at '{audio_file_path}'.")
for doc in all_document:
    print(doc.keys())






