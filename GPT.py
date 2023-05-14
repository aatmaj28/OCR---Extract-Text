import cv2
import pytesseract

# Load the image using OpenCV
img = cv2.imread("image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Pass the image through OCR (Optical Character Recognition) using the pytesseract library
text = pytesseract.image_to_string(gray)

# Print the extracted text
print(text)
