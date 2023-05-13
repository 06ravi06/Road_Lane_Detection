# Road_Lane_Detection


This code demonstrates lane detection on an image and a video using OpenCV in Python.

The code loads an image and applies various image processing techniques such as converting the image to grayscale, applying Gaussian blur, and Canny edge detection. It then defines the region of interest and applies it to the image using a masking technique. The Hough transform is applied to the masked image to detect the lines and draws the detected lines on the original image. The result is displayed using Matplotlib.

The same procedure is applied to a video where each frame of the video is processed using the above-described steps, and the detected lines are drawn on each frame of the video. The output video is saved with the detected lines on it.

The code has several functions such as the "roi" function for defining the region of interest, "draw_lines" function for drawing detected lines on the image, and "process_frame" function for processing each frame of the video.


## Functions used OpenCV


This code is a Python script for detecting lane lines in a video using computer vision techniques. It uses the OpenCV library to apply Gaussian blur, Canny edge detection, and Hough transform to the frames of a given video, to detect the lane lines. It then draws the detected lane lines on the original video frames and outputs the resulting video as a new file. The script includes functions for defining the region of interest (ROI), drawing the detected lines, and processing individual frames of the video.


The code is well-documented with comments explaining each step of the process. It also includes examples of how to use the OpenCV library functions, such as cv2.imread(), cv2.cvtColor(), cv2.GaussianBlur(), cv2.Canny(), cv2.HoughLinesP(), and cv2.line(). Additionally, it includes functions for drawing lines on the video frames and defining the ROI


## OUTPUT

<div align="center">

![Image_Output](https://github.com/06RAVI06/Road_Lane_Detection/assets/107626246/f7277bae-1288-4f69-b6f6-07e9ddb3d982)

https://github.com/06RAVI06/Road_Lane_Detection/assets/107626246/1ec38563-3422-4dd5-90a1-ebeb8595923e

</div>
