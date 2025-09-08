from app.services.data_retrieval.conigurations import JSON_SCHEMA
import os
import datetime


class DataRetrievalHelper:

    @staticmethod
    def get_specific_metadata(file_path):
        data_json = JSON_SCHEMA
        file_stats = os.stat(file_path)

        data_json['name'] = os.path.basename(file_path)
        data_json['size'] = file_stats.st_size
        data_json['last_modified_time'] = datetime.datetime.fromtimestamp(file_stats.st_mtime)
        data_json['path'] = file_path

        return data_json




