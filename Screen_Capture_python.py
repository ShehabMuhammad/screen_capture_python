import numpy as np
import cv2, random. time
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(f"output_Date_{time.strftime('%Y_%m_%d_%H_%M_%S')}_ID_{random.random()}.avi", fourcc, 25.0, (1366, 768))

while 1:
	img = ImageGrab.grab()
	img_np = np.array(img)
	frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
	cv2.imshow("Captured frame..", frame)
	output.write(frame);  
	if cv2.waitKey(1) == 27:
		break

out.release()
cv2.destroyAllWindows()
