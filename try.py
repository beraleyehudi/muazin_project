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
file_stats = os.stat(file_path)
print(f"File Name: {os.path.basename(file_path)}")
print(f"File Size: {file_stats.st_size} bytes")
print(f"Last Modified Time: {datetime.datetime.fromtimestamp(file_stats.st_mtime)}")
print(
    f"Creation Time (on Unix/macOS, this is often the last modified time): {datetime.datetime.fromtimestamp(file_stats.st_ctime)}")
# print(f"Last Access Time: {datetime.datetime.fromtimestamp(file_stats.st_atime)}")
# print(f"Permissions (st_mode): {oct(file_stats.st_mode)}")
# print(f"Inode Number (st_ino): {file_stats.st_ino}")
# print(f"Device ID (st_dev): {file_stats.st_dev}")
# print(f"Number of Hard Links (st_nlink): {file_stats.st_nlink}")
# print(f"User ID of Owner (st_uid): {file_stats.st_uid}")
# print(f"Group ID of Owner (st_gid): {file_stats.st_gid}")