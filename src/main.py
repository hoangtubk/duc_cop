import numpy as np
import cv2

class duc_cop():
    def __init__(self, path_image):
        self._white_pixel = 255
        self._img = cv2.imread(path_image)

    def get_location(self, matrix=(100, 100)):
        height, width, channels = self._img.shape
        print(self._img[0][0][2])
        print(self._img.shape)
        for h in range(0, height - matrix[0]):
            for w in range(0, width - matrix[1]):
                mt = self._img[h:h + matrix[0], w: w + matrix[1]]
                # print(mt)
                if (mt==255).all():
                    print(h, w)
                    assert False

    def write_matrix_image(self):
        height, width, channels = self._img.shape
        file_R = open('file_R.txt', 'a')
        file_G = open('file_G.txt', 'a')
        file_B = open('file_B.txt', 'a')
        for h in range(0, height):
            for w in range(0, width):
                file_R.write(str(self._img[h, w, 0]) + ' ')
                file_G.write(str(self._img[h, w, 1]) + ' ')
                file_B.write(str(self._img[h, w, 2]) + ' ')
            file_R.write('\n')
            file_G.write('\n')
            file_B.write('\n')

    def find_contour(self, height, weight):
        im = cv2.imread('image.jpg')
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 250, 250, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(im, contours, -1, (0, 255, 0), 3)

        for i in range(0, len(contours)):
            x, y, w, h = cv2.boundingRect(contours[i])
            if (h, w) == (height, weight):
                print(x, y, w, h)
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
                break
        cv2.imshow('image', im)
        cv2.waitKey(0)

        return x, y

    def bounding_rect(self):
        img = cv2.imread('star.jpg', 0)
        ret, thresh = cv2.threshold(img, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, 1, 2)
        cnt = contours[0]
        M = cv2.moments(cnt)
        print(M)

    def insert_img(self, path_src, path_des, size=(100, 100), coord=(0, 0)):
        img_src = cv2.imread(path_src)
        img_des= cv2.imread(path_des)

        dst = cv2.resize(img_src, size, interpolation=cv2.INTER_CUBIC)
        img_des[coord[0]:coord[0] + size[0], coord[1]:coord[1] + size[1]] = dst[:,:]
        cv2.imshow('image', img_des)
        cv2.waitKey(0)

if __name__ == '__main__':
    test = duc_cop(path_image='image.jpg')
    # test.get_location((110,110))
    # test.write_matrix_image()
    x, y = test.find_contour(100, 100)
    test.insert_img('haha.png', 'image.jpg', coord=(y, x))

    print(x, y)
