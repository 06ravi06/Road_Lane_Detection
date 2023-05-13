import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("src/pexels-photo-1955134.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define ROI function
def roi(image, vertices):
    mask = np.zeros_like(image)
    mask_color = 255
    cv2.fillPoly(mask, vertices, mask_color)
    return cv2.bitwise_and(image, mask)

# Define draw lines function
def draw_lines(image, hough_lines):
    for line in hough_lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 5)
    return image

# Process image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
blur_gray = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur_gray, 50, 150)
vertices = np.array([[(0, img.shape[0]), (img.shape[1]/2, img.shape[0]/2+50), (img.shape[1], img.shape[0])]], dtype=np.int32)
masked_edges = roi(edges, vertices)
lines = cv2.HoughLinesP(masked_edges, 2, np.pi/180, 15, np.array([]), 40, 20)
line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
draw_lines(line_img, lines)
lines_edges = cv2.addWeighted(img, 0.8, line_img, 1, 0)

# Display results
plt.imshow(lines_edges)
plt.show()
def draw_lines_video(img, lines, color=[255, 0, 0], thickness=2):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked
def process_frame(frame):
    # Convert to grayscale, apply Gaussian blur and Canny edge detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur_gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur_gray, 50, 150)

    # Define ROI vertices and apply ROI
    imshape = frame.shape
    vertices = np.array([[(0, imshape[0]), (imshape[1] * 0.4, imshape[0] * 0.6), (imshape[1] * 0.6, imshape[0] * 0.6), (imshape[1], imshape[0])]], dtype=np.int32)
    masked_edges = cv2.fillPoly(np.zeros_like(edges), vertices, 255)
    masked_edges = cv2.bitwise_and(edges, masked_edges)

    # Apply Hough transform
    lines = cv2.HoughLinesP(masked_edges, rho=2, theta=np.pi/180, threshold=15, minLineLength=40, maxLineGap=20)

    # Draw lines on original image
    line_img = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_img, (x1, y1), (x2, y2), (255, 0, 0), 5)

    # Combine line image with original image
    lines_edges = cv2.addWeighted(frame, 0.8, line_img, 1, 0)
    return lines_edges

# Load video
cap = cv2.VideoCapture("src/road-1101.mp4")

while cap.isOpened():
    # Read frame from video
    ret, frame = cap.read()
    if not ret:
        break

    # Process frame and display
    lines_edges = process_frame(frame)
    cv2.imshow("Lane detection", lines_edges)

    # Quit on 'q' press
    if cv2.waitKey(100) == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
