import cv2
import numpy as np
canvas=np.zeros((512,512,3),np.uint8) + 255

font1=cv2.FONT_HERSHEY_SIMPLEX
font2=cv2.FONT_HERSHEY_COMPLEX
font3=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(canvas,"sude",(100,200),font1,4,(255,255,100),cv2.LINE_AA)
#tuval,yazılacak metin,başlangıç kordinantı,yazı şekli,kalınlık,renk,yazı tipi(varsayılan)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()