from app.connections import MongoConnection
from app.dal import MongoDal
import pymongo
import gridfs
from datetime import datetime
import os
from bson import binary

dal = MongoDal(MongoConnection())

document = {'name':'berale', 'age':22}

# async def cc():
#
#     await dal.insert_document('audio', document)
#
# cc()
# coll = MongoConnection().get_db_collection('audio')
#

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["muazin"]

fs = gridfs.GridFS(db)

# Path to your WAV file
wav_file_path = r'C:\Users\User\Desktop\podcasts\download (8).wav'
# def insert_by_gridfs():
#
#     try:
#         with open(wav_file_path, 'rb') as f:
#             # Put the file into GridFS
#             file_id = fs.put(f)
#             print(f"Large WAV file inserted with GridFS file_id: {file_id}")
#
#     except FileNotFoundError:
#         print(f"Error: WAV file not found at {wav_file_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

def audio_to_bytes():
    # return 'rereer'
    with open(wav_file_path, 'rb') as f:
        a = f.read()
    return a

def calculate_unique_id(metadata) -> float:
    return datetime.timestamp(metadata['last_modified_time']) * metadata['size']

def get_specific_metadata(file_path):
    data_json = {}
    file_stats = os.stat(file_path)

    data_json['name'] = os.path.basename(file_path)
    data_json['size'] = file_stats.st_size
    data_json['last_modified_time'] = datetime.fromtimestamp(file_stats.st_mtime)
    data_json['path'] = file_path

    return data_json



coll = db["audio"]
coll.insert_one({'_id':calculate_unique_id(get_specific_metadata(wav_file_path)), 'data':audio_to_bytes()})

# print(dict(coll.find()))
# for doc in coll.find():
#     print(doc)
# dal.insert_document('audio', document)