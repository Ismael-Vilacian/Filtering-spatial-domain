import cv2

class Sharpness():
    def __init__(self, filter_value, image_name):
        self.filter_value = filter_value
        self.image_name = f'images/{image_name}'

    def sharpness_filter(self):

        image_cv2 = cv2.imread(self.image_name)
        blurred = cv2.GaussianBlur(image_cv2, (self.filter_value, self.filter_value), 0)
        mask = cv2.subtract(image_cv2, blurred)

        sharpened_image = cv2.add(image_cv2, mask)

        cv2.imwrite("processed_images/Realçada_nitidez.png", sharpened_image)