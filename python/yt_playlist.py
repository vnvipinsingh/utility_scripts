from pytube import Playlist, YouTube

playlist_url = input("Enter Playlist's Url: ").strip()
downloaded_till = input('How many videos have been downloaded successfully: ')
downloaded_till = int(downloaded_till)
url_list = []

def download_video(index, url):
    yt = YouTube(url=url)
    stream = yt.streams.get_by_itag(22)
    print(f'Downloading {index}: {yt.title}')
    stream.download()
    print(f'Downloaded succecfully')

p = Playlist(url=playlist_url)
for url in p.video_urls: url_list.append(url)
print(f'Playlist: {p.title}')

for i, url in enumerate(url_list):
    if i < downloaded_till: continue
    download_video(i+1, url)