# -*- coding: utf-8 -*-
"""MTCNN

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y-HflNgrTACQkECzxWgUfLX7dCteZk0A
"""

# Install library MTCNN
!pip install mtcnn

# Import required libraries
from mtcnn.mtcnn import MTCNN
import cv2
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/people.jpeg'  # Ganti dengan jalur yang benar jika perlu
image = cv2.imread(image_path)

# Check if the image was loaded properly
if image is None:
    print("Error: Gambar tidak ditemukan atau tidak dapat dimuat.")
else:
    # Convert image to RGB (MTCNN works better with RGB format)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Initialize the MTCNN detector
    detector = MTCNN()

    # Detect faces in the image
    faces = detector.detect_faces(image_rgb)

    # Check if faces are detected
    if len(faces) == 0:
        print("Tidak ada wajah yang terdeteksi.")
    else:
        print(f"Wajah yang terdeteksi: {len(faces)}")

    # Draw bounding boxes and keypoints on detected faces
    for face in faces:
        bounding_box = face['box']
        keypoints = face['keypoints']

        # Draw bounding box
        cv2.rectangle(
            image,
            (bounding_box[0], bounding_box[1]),
            (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
            (0, 255, 0),  # Warna hijau untuk kotak
            2
        )

        # Draw facial keypoints
        cv2.circle(image, keypoints['left_eye'], 2, (0, 255, 255), 2)
        cv2.circle(image, keypoints['right_eye'], 2, (0, 255, 255), 2)
        cv2.circle(image, keypoints['nose'], 2, (0, 255, 255), 2)
        cv2.circle(image, keypoints['mouth_left'], 2, (0, 255, 255), 2)
        cv2.circle(image, keypoints['mouth_right'], 2, (0, 255, 255), 2)

    # Show the result with bounding boxes
    cv2_imshow(image)# Install library MTCNN

!pip install mtcnn

# Import required libraries
from mtcnn.mtcnn import MTCNN
import cv2
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/people.jpeg'  # Ganti dengan jalur yang benar jika perlu
image = cv2.imread(image_path)

# Check if the image was loaded properly
if image is None:
    print("Error: Gambar tidak ditemukan atau tidak dapat dimuat.")
else:
    # Convert image to RGB (MTCNN works better with RGB format)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Initialize the MTCNN detector
    detector = MTCNN()

    # Detect faces in the image
    faces = detector.detect_faces(image_rgb)

    # Check if faces are detected
    if len(faces) == 0:
        print("Tidak ada wajah yang terdeteksi.")
    else:
        print(f"Wajah yang terdeteksi: {len(faces)}")

    # Draw bounding boxes and keypoints on detected faces
    for face in faces:
        bounding_box = face['box']
        keypoints = face['keypoints']

        # Draw bounding box
        cv2.rectangle(
            image,
            (bounding_box[0], bounding_box[1]),
            (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
            (0, 255, 0),  # Warna hijau untuk kotak
            2
        )

        # Draw facial keypoints
        cv2.circle(image, keypoints['left_eye'], 2, (0, 255, 255), 2)
        cv2.circle(image, keypoints['right_eye'], 2, (0, 255, 255), 2)
        cv2.circle(image, keypoints['nose'], 2, (0, 255, 255), 2)
        cv2.circle(image, keypoints['mouth_left'], 2, (0, 255, 255), 2)
        cv2.circle(image, keypoints['mouth_right'], 2, (0, 255, 255), 2)

    # Show the result with bounding boxes
    cv2_imshow(image)