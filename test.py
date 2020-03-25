from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import machinevision as mv

# test itpl (2D-Interpolation)
print(mv.itpl(0,1,0,1,0,1,2,3,[0.3, 0.7]))
print(mv.itpl(0,1,0,1,0,1,3,2,[0.3, 0.7]))

# reading an Image
I_PIL = Image.open('cat.jpg')
I = np.array(I_PIL)

plt.figure('Image')
plt.imshow(I)
plt.axis('off')
plt.show()
I_pil = Image.fromarray(np.uint8(I))
I_pil.save('cat_save.png')

# test rgb2gray (colorful image to gray value image)
I_gray = mv.rgb2gray(I)

plt.figure('Gray Image')
plt.imshow(I_gray, cmap = "gray")
plt.axis('off')
plt.show()
I_gray_pil = Image.fromarray(np.uint8(I_gray))
I_gray_pil.save('cat_gray.png')

# test imrotate (rotating an Image)
I_rotate = mv.imrotate(I_gray, np.pi/8)
plt.figure('Rotate Image')
plt.imshow(I_rotate, cmap = "gray")
plt.axis('off')
plt.show()
I_rotate_pil = Image.fromarray(np.uint8(I_rotate))
I_rotate_pil.save('cat_rotate.png')

# test imscale (scaling an Image)
I_scale = mv.imscale(I_gray, 0.8, 1.3)
plt.figure('Scale Image')
plt.imshow(I_scale, cmap = "gray")
plt.axis('off')
plt.show()
I_scale_pil = Image.fromarray(np.uint8(I_scale))
I_scale_pil.save('cat_scale.png')
