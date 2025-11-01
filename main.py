import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Get image dimensions
height, width, _ = image.shape

# Annotate the image with its width
annotated_image = image.copy()
text = f'Width: {width}px'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 255, 0)  # Green
thickness = 2
position = (10, 50)

cv2.putText(annotated_image, text, position, font, font_scale, color, thickness)

# Convert BGR to RGB for displaying with matplotlib
annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

# Display the annotated image
plt.imshow(annotated_image_rgb)
plt.axis('off')
plt.title('Annotated Image')
plt.show()
