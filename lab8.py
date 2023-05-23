'''import cv2
import time

def image_processing():
    img = cv2.imread('img_teat.jpg')
    #cv2.imshow('image', img)
    #w, h = img.shape[:2]
    #(cX, cY) = (w // 2, h // 2)
    #M = cv2.getRotationMatrix((cX, cY), 45, 1.0)
    #rotated = cv2.warpAffline(img, M, (w, h))
    #cv2.imshow('rotated', rotated)

    #cat = img[250:580, 20:280]
    #cv2.imshow('image', cat)

    #r = cv2.selectROI(img)
    #image_cropped = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0] + r[2])]
    #cv2.imshow('cropped', image)

    cv2.line(img)

if __name__ == '__main__':
    image_processing()

cv2.waitKey(0)
cv2.destroyAllWindows()'''



def video_processing():
    cap = cv2.VideoCapture(1)
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
    frame = cv2.resize(frame, down_points, interpolation=cv2.Inter)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findCountours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
    c = max(contours, key = cv2.contourArea)
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle()







