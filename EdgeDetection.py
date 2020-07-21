print('Importing Library...')
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load image
img_path = 'Images/hand.jpg'
print(f'Detecting for {img_path}')
image = cv2.imread(img_path)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image = cv2.resize(image,dsize=(500,500))

def detectEdge(insert_images):
    # Copy to avoid destructive move
    source_image = insert_images.copy()
    
    # Calculate for threshold
    medium_value = np.median(source_image)
    lower_value = int(max(0,0.7*medium_value))
    upper_value = int(min(255,1.3*medium_value))
    
    # Use Canny Edge Detection
    edge = cv2.Canny(source_image,threshold1=lower_value,threshold2=upper_value)
    source_image[edge == 255] = [0,255,0]
    plt.imshow(source_image)
    plt.show()

detectEdge(image)