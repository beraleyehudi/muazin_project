from datetime import datetime
class DataLoaderHelper:

    @staticmethod
    def calculate_unique_id(metadata) -> float:
        return datetime.timestamp(metadata['last_modified_time']) * metadata['size']

    @staticmethod
    def audio_to_bytes(wav_file_path):
        with open(wav_file_path, 'rb') as f:
            return f.read()







