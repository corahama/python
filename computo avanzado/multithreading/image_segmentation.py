import numpy as np
import cv2

from kmeans_multiprocessing import run

K = 2
path = 'multithreading/data/image.jpg'

img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
twoDimage = img.reshape((-1,3))
twoDimage = np.float32(twoDimage)

means = run(twoDimage, K)
means = np.uint8(means)
labels = np.array(list(map(lambda e: np.argmin(tuple(np.linalg.norm(e-mean) for mean in means)),
    twoDimage)))
res = means[labels]
result_image = res.reshape((img.shape))

result_image = cv2.cvtColor(result_image, cv2.COLOR_RGB2BGR)
cv2.imwrite('multithreading/data/result-img.jpg', result_image)
