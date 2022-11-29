import cv2
image=cv2.imread("solar-system.jpg")

cv2.putText(image,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(image,
           "Mercury",
           (100,300),
           cv2.FONT_HERSHEY_SIMPLEX,
           0.5,
           (255,255,255)
           )

cv2.putText(image,
           "Venus",
           (200,300),
           cv2.FONT_HERSHEY_SIMPLEX,
           0.5,
           (255,255,255)
           )

cv2.putText(image,
           "Earth",
           (300,300),
           cv2.FONT_HERSHEY_SIMPLEX,
           0.5,
           (255,255,255)
           )

cv2.putText(image,
           "Mars",
           (400,300),
           cv2.FONT_HERSHEY_SIMPLEX,
           0.5,
           (255,255,255)
           )
cv2.putText(image,
           "Jupiter",
           (500,300),
           cv2.FONT_HERSHEY_SIMPLEX,
           0.5,
           (255,255,255)
           )
cv2.putText(image,
           "Saturn",
           (800,300),
           cv2.FONT_HERSHEY_SIMPLEX,
           0.5,
           (255,255,255)
           )
cv2.putText(image,
           "Uranus",
           (1000,300),
           cv2.FONT_HERSHEY_SIMPLEX,
           0.5,
           (255,255,255)
           )
cv2.putText(image,
           "Neptune",
           (1150,300),
           cv2.FONT_HERSHEY_SIMPLEX,
           0.5,
           (255,255,255)
           )

cv2.imshow("output",image)
cv2.waitKey(0)
