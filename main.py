import pytube

video_list = []

print("Enter links of videos(when finished type 'OK')")

while True:
    url = input("")
    if url == 'OK':
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    v = pytube.YouTube(video)
    stream = v.streams.get_by_itag(22)
    print(f"Downloading your  Video {x}.........")
    stream.download()
    print("Done")


