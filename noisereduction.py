import cv2

def noise_reduction(img_0):
    img = cv2.imread(img_0,0)

    # Otsu's thresholding after medianBlur
    blur=cv2.medianBlur(img,5)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return th3
