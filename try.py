import os
from itertools import count

counter = 0
for entry in os.listdir(r'C:\Users\User\Desktop\podcasts'):
    print(os.path.join(r'C:\Users\User\Desktop\podcasts', entry))
    counter += 1

print('-'*10, counter)