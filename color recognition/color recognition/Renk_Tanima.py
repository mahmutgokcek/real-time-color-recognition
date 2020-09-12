import os
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    acik_sari= np.array([25, 146, 190])
    koyu_sari= np.array([100, 190, 250])
    sari_mask=cv2.inRange(hsv_frame, acik_sari,koyu_sari)
    sari = cv2.bitwise_and(frame, frame, mask=sari_mask)

    acik_kirmizi = np.array([161, 155, 84])
    koyu_kirmizi = np.array([179, 255, 255])
    kirmizi_mask = cv2.inRange(hsv_frame, acik_kirmizi, koyu_kirmizi)
    kirmizi = cv2.bitwise_and(frame, frame, mask=kirmizi_mask)
    
    acik_mavi = np.array([94, 80, 2])
    koyu_mavi = np.array([126, 255, 255])
    mavi_mask = cv2.inRange(hsv_frame, acik_mavi, koyu_mavi)
    mavi = cv2.bitwise_and(frame, frame, mask=mavi_mask)

   
    acik_yesil = np.array([25, 52, 72])
    koyu_yesil = np.array([102, 255, 255])
    yesil_mask = cv2.inRange(hsv_frame, acik_yesil, koyu_yesil)
    yesil = cv2.bitwise_and(frame, frame, mask=yesil_mask)

    
    acik = np.array([0, 42, 0])
    koyu = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, acik, koyu)
    sonuc = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Kirmizi", kirmizi)
    cv2.imshow("Mavi", mavi)
    cv2.imshow("Yeşil", yesil)
    cv2.imshow("Sari",sari)
    cv2.imshow("Diger Renkler", sonuc)

    font = cv2.FONT_HERSHEY_COMPLEX

    if int(cv2.__version__[0]) > 3:
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    else:
        _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

            if len(approx) == 3:
                cv2.putText(frame, "Ucgen", (x, y), font, 1, (0, 0, 0))
            elif len(approx) == 4:
                cv2.putText(frame, "Dikdortgen", (x, y), font, 1, (0, 0, 0))


    cv2.imshow("Sekilleri Algila", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
