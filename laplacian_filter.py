import cv2

class Laplacian():
    def __init__(self, image_name):
        self.image_name = f'images/{image_name}'
    
    def laplacian_filter(self):
        image = cv2.imread(self.image_name, cv2.IMREAD_GRAYSCALE)

        laplacian = cv2.Laplacian(image, cv2.CV_64F)

        cv2.imwrite('processed_images/laplacian.png', laplacian)