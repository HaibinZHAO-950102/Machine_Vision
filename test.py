from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import machinevision as mv

# test itpl (2D-Interpolation)
# print(mv.itpl(0,1,0,1,0,1,2,3,[0.3, 0.7]))
# print(mv.itpl(0,1,0,1,0,1,3,2,[0.3, 0.7]))

# reading an Image
I_PIL = Image.open('cat.jpg')
I = np.array(I_PIL)

# plt.figure('Image')
# plt.imshow(I)
# plt.axis('off')
# plt.show()
# I_pil = Image.fromarray(np.uint8(I))
# I_pil.save('cat_save.png')

# test rgb2gray (colorful image to gray value image)
I_gray = mv.rgb2gray(I)

# plt.figure('Gray Image')
# plt.imshow(I_gray, cmap = "gray")
# plt.axis('off')
# plt.show()
# I_gray_pil = Image.fromarray(np.uint8(I_gray))
# I_gray_pil.save('cat_gray.png')

# test imrotate (rotating an Image)
# I_rotate = mv.imrotate(I_gray, np.pi/8)
# plt.figure('Rotate Image')
# plt.imshow(I_rotate, cmap = "gray")
# plt.axis('off')
# plt.show()
# I_rotate_pil = Image.fromarray(np.uint8(I_rotate))
# I_rotate_pil.save('cat_rotate.png')
#
# # test imscale (scaling an Image)
# I_scale = mv.imscale(I_gray, 0.8, 1.3)
# plt.figure('Scale Image')
# plt.imshow(I_scale, cmap = "gray")
# plt.axis('off')
# plt.show()
# I_scale_pil = Image.fromarray(np.uint8(I_scale))
# I_scale_pil.save('cat_scale.png')

# test gammacorrection
I_gamma_1 = mv.gammacorrection(I_gray, 4)
I_gamma_2 = mv.gammacorrection(I_gray, 0.1)
# plt.figure('Gamma Correction')
# plt.subplot(1,2,1)
# plt.imshow(I_gamma_1, cmap = "gray")
# plt.axis('off')
# plt.subplot(1,2,2)
# plt.imshow(I_gamma_2, cmap = "gray")
# plt.axis('off')
# plt.show()
# I_gamma_1_pil = Image.fromarray(np.uint8(I_gamma_1))
# I_gamma_2_pil = Image.fromarray(np.uint8(I_gamma_2))
# I_gamma_1_pil.save('I_gamma_1.png')
# I_gamma_2_pil.save('I_gamma_2.png')

# test histogramm
# H_1 = mv.histogramm(I_gamma_1)
# H_2 = mv.histogramm(I_gamma_2)
# H_3 = mv.histogramm(I_gray)
# plt.figure('Histogramm')
# plt.subplot(1,3,1)
# plt.bar(range(len(H_1)), H_1)
# plt.xlim((0, 255))
# plt.xticks([0, 32, 64, 96, 128, 160, 192, 224, 255])
# plt.subplot(1,3,2)
# plt.bar(range(len(H_2)), H_2)
# plt.xlim((0, 255))
# plt.xticks([0, 32, 64, 96, 128, 160, 192, 224, 255])
# plt.subplot(1,3,3)
# plt.bar(range(len(H_3)), H_3)
# plt.xlim((0, 255))
# plt.xticks([0, 32, 64, 96, 128, 160, 192, 224, 255])
# plt.show()

# test hdri (high dynamic range imaging)
I_hdri = mv.hdri(I_gray, I_gamma_1, I_gamma_2)
