import numpy as np
from PIL import Image


density = 0.001
h = 256
w = 256
c = 3

mean = 0
variance = 1
amplitude = 2

img = Image.open('datasets/summer2winter_yosemite/testB/2007-05-02 01_07_01.jpg')
# img.show()

img1 = np.array(img)
Nd = density
Sd = 1 - Nd
mask = np.random.choice((0, 1, 2), size=(h, w, 1), p=[Nd/2.0, Nd/2.0, Sd])      # 生成一个通道的mask
mask = np.repeat(mask, c, axis=2) # 在通道的维度复制，生成彩色的mask

img1[mask == 0] = 0                                                              # 椒
img1[mask == 1] = 255                                                            # 盐
img1= Image.fromarray(img1.astype('uint8')).convert('RGB')
img1.save(r'D:\sjtu\2020~2021-1\人工智能理论与应用\12-GAN\cycleGAN-and-pix2pix\report\saltpepper.png')


img2 = np.array(img)
N = amplitude * np.random.normal(loc=mean, scale=variance, size=(h, w, 1))
N = np.repeat(N, c, axis=2)
img2 = N + img2
N= Image.fromarray(N.astype('uint8')).convert('RGB')
N.save(r'D:\sjtu\2020~2021-1\人工智能理论与应用\12-GAN\cycleGAN-and-pix2pix\report\gaussian.png')
img2[img2 > 255] = 255  # 避免有值超过255而反转
img2 = Image.fromarray(img2.astype('uint8')).convert('RGB')
img2.save(r'D:\sjtu\2020~2021-1\人工智能理论与应用\12-GAN\cycleGAN-and-pix2pix\report\gaussianimg.png')

