import cv2

img = cv2.imread("solar-system.jpg")



cv2.putText(
    img,
    "Sun",
    (70,80),
    cv2.FONT_HERSHEY_COMPLEX,
    2,
    (0,0,255)
)

cv2.putText(
    img,
    "Mercury",
    (110,200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (127,127,127)
)

cv2.putText(
    img,
    "Venus",
    (190,195),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (130,186,20)
)

cv2.putText(
    img,
    "Earth",
    (290,190),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    "Mars",
    (380,205),
    cv2.FONT_HERSHEY_COMPLEX,
    0.45,
    (10,255,210)
)

cv2.putText(
    img,
    "Jupiter",
    (450,110),
    cv2.FONT_HERSHEY_COMPLEX,
    1.75,
    (210,130,30)
)

cv2.putText(
    img,
    "Jupiter",
    (450,110),
    cv2.FONT_HERSHEY_COMPLEX,
    1.75,
    (210,130,30)
)

cv2.putText(
    img,
    "Saturn",
    (740,180),
    cv2.FONT_HERSHEY_COMPLEX,
    0.75,
    (130,255,60)
)

cv2.putText(
    img,
    "Uranus",
    (954,180),
    cv2.FONT_HERSHEY_COMPLEX,
    0.65,
    (255,115,60)
)

cv2.putText(
    img,
    "Neptune",
    (1100,180),
    cv2.FONT_HERSHEY_COMPLEX,
    0.65,
    (255,255,255)
)
cv2.imshow("output", img)
cv2.waitKey(0)
