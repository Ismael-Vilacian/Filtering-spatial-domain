import cv2

class Smoothing():
    def __init__(self, filter_value, image_name, filter_type):
        self.filter_value = filter_value
        self.image_name = f'images/{image_name}'
        self.filter_type = filter_type
    
    def smoothing_filter(self):
        image = cv2.imread(self.image_name)

        filtered_image_mean = cv2.blur(image, (self.filter_value, self.filter_value))

        filtered_image_median = cv2.medianBlur(image, self.filter_value)

        filtered_image_gaussian = cv2.GaussianBlur(image, (self.filter_value, self.filter_value), 0)

        if self.filter_type == 1:
            cv2.imwrite('processed_images/Media_smoothing.png', filtered_image_mean)
        elif self.filter_type == 2:
            cv2.imwrite('processed_images/Mediana_smoothing.png', filtered_image_median)
        elif self.filter_type == 3:
            cv2.imwrite('processed_images/Gaussiano_smoothing.png', filtered_image_gaussian)