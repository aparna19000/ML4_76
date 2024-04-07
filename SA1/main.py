from cvzone.FaceDetectionModule import FaceDetector
import cv2
import numpy as np

# Capture the web cam video feed


# Create a detector using FaceDetector


while True:
    try:
        # Read single image from the captured feed and store it in img variable
        
        # Flip the imgage
        
        # Use detector to find faces in the image and store it in bboxs variable
        

        # Check if bboxs exits
        
            # Traverse throught each box in the bboxs
            
                # Get X, Y, W, H of the box
                

                # Draw the rectangle using X, Y, W, H to show rectangle on detected face
                
            
        # Display the image    
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print("Exception", e)

cv2.destroyAllWindows()
