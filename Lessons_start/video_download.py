import requests



url = "https://parsinger.ru/video_downloads/videoplayback.mp4"

# response = requests.get(url=url, stream=True)
# with open('videoplayback.mp4', 'wb') as file:
#     file.write(response.content)

response = requests.get(url=url, stream=True)
with open('videoplayback.mp4', 'wb') as video:
    for piece in response.iter_content(chunk_size=100000):
        video.write(piece)




