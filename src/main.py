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
                print(mt)
                assert False
                if (mt==255).all():
                    print(h, w)
                    assert False

if __name__ == '__main__':
    test = duc_cop(path_image='image.jpg')
    test.get_location((25,25))

