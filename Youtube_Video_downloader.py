from pytube import YouTube

yt = YouTube(input("Enter the YouTube Video link to Download the video: "))

print(yt.title)

print(yt.thumbnail_url)

print(yt.streams.filter(only_audio = True))

download_video = yt.streams.get_highest_resolution()


download_video.download()
