import os
import time

print(os.getcwd())
os.chdir('D:\\luk')
print(os.getcwd())
os.mkdir('nowy_folder')
time.sleep(3)
os.rename('nowy_folder', 'nowszy_folder')
time.sleep(3)
os.rmdir('nowszy_folder')

