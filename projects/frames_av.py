import av

container = av.open('video.mp4')
container.seek(int(container.duration/2))
generator = container.decode()
frame = generator.__next__()
frame.to_image().save('image.jpg')