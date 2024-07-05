import easyocr
from noisereduction import noise_reduction
import matplotlib.pyplot as plt


img_0=input('Input path of img\n')
img=noise_reduction(img_0)
reader = easyocr.Reader(['en'],gpu=False)
horizontal_list, free_list = reader.detect(img, optimal_num_chars=6)
character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
allow_list = list(character)
allow_list.extend(list(character.lower()))
result = reader.recognize(img,
                          allowlist=allow_list,
                          horizontal_list=horizontal_list[0],
                          free_list=free_list[0],
                          detail=0)
plt.imshow(img,'gray')
plt.show()
result = reader.readtext(img)
print(result)

