import pytube


link = input("Enter Youtube video link:  ")

yt = pytube.YouTube(link)

stream = yt.streams.first()

stream.download()
