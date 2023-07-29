from os import path, getcwd, rename
from pytube import Playlist, YouTube

playlist_url = input("Enter Playlist's Url: ")
prefix = input('Enter Prefix: ')
renamed_till = input('How many videos have been renamed successfully: ')
renamed_till = int(renamed_till)

invalid_char = ["'", '"', '\\', '/', ':', '*', '?', '<', '>', '|', '.', ',', ]
titles = []

def remove_invalid_char(title):
    title = title.strip()
    for c in invalid_char: 
        title = title.replace(c, '')
    return title

        
def rename_file(directory, name, new_name):
        old_path = path.join(directory, name)
        new_path = path.join(directory, new_name)
        rename(old_path, new_path)

p = Playlist(url=playlist_url)
print(f'Playlist: {p.title}')
for url in p.video_urls:
    yt = YouTube(url)
    titles.append(yt.title)

for i, title in enumerate(titles):
    if(i < renamed_till): continue
    name = remove_invalid_char(title) + '.mp4'
    infix = '-' + str(101+i) + '-'
    new_name = prefix + infix + name
    rename_file(getcwd(), name, new_name)
    print(f"Renamed {i+1}: '{name}' '{new_name}'")