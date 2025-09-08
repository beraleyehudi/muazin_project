import os
import datetime
from itertools import count

# counter = 0
# for entry in os.listdir(r'C:\Users\User\Desktop\podcasts'):
#     print(os.path.join(r'C:\Users\User\Desktop\podcasts', entry))
#     counter += 1
#
# print('-'*10, counter)
file_path = r'C:\Users\User\Desktop\podcasts\download (4).wav'
data_json = {}
file_stats = os.stat(file_path)

# data_json['name'] = os.path.basename(file_path)
data_json['size'] = file_stats.st_size
data_json['last_modified_time'] = datetime.datetime.fromtimestamp(file_stats.st_mtime)
data_json['path'] = file_path

print(data_json)
print(datetime.datetime.timestamp(data_json['last_modified_time']) * data_json['size'])
# print(type(int(data_json['last_modified_time'])))