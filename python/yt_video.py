from pytube import YouTube

video_url = input("Enter Video's Url: ").strip()

def download_video(url):
    yt = YouTube(url=url)
    stream = yt.streams.get_by_itag(22)
    print(f'Downloading: {yt.title}')
    stream.download()
    print(f'Downloaded succecfully')

download_video(url=video_url)