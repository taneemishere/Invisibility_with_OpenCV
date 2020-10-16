# Invisibility_with_OpenCV
A python application that using the power of OpenCV to simulate the invisibility of 
someone during the live webcam stream.

## Requirements
- OpenCV
- Numpy

## The Code Flow

- Import some of the libraries we need for this script
- Capture the webcam with OpenCV
- Iterate 30 times capturing from webcam as we'll have a static background
- If something unknown happens, break out of the loop
- Flip the image, as to see how we see our image in the mirror
