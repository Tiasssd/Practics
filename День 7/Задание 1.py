# -*- coding: 1251 -*-
import cv2



# �������� �����������
image = cv2.imread(r"C:\Users\shekh\Downloads\Telegram Desktop\DSCN4843.JPG")

font                   = cv2.FONT_HERSHEY_COMPLEX_SMALL
bottomLeftCornerOfText = (300,500)
fontScale              = int(input('������� ������ ������: '))
r, g, b = map(int,input('������� ������ ����: ').split())
fontColor = (r,g,b)
thickness              = 25
lineType               = 2

cv2.putText(image,'Shekh', 
    bottomLeftCornerOfText,
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)

cv2.putText(image,'M', 
    (2400,1350),
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)

cv2.putText(image,'I', 
    (3100,1750),
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)

# ������� ����������� �� 90 �������� �� ������� �������
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# �������� ��������� ���������
gray_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)
final_image = cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2BGR)

cv2.namedWindow('��� ����', cv2.WINDOW_NORMAL)  # WINDOW_NORMAL ��������� �������� ������ ����

# ��������� ������� ���� (������, ������)
cv2.resizeWindow('��� ����', 800, 600)  # ��������� ��������
# ���������� ����������
cv2.imwrite("obr1.jpg", final_image)
cv2.imwrite("image.jpg", image)
cv2.imshow('��� ����', image)
cv2.waitKey(0)  # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()