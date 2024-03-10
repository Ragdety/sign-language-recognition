import cv2
import os
import uuid
import time

images_path = 'Tensorflow\workspace\images\collected_images'

labels = ['Hello']
number_imgs = 15 #12 train and 3 test

for label in labels:
    os.mkdir('C:\\Users\\desktop\\Documents\\awl-Nishchay-intern-work\\GrizzHacks\\RealTimeObjectDetection\\Tensorflow\\workspace\\images\\collected_images'+label)
    # os.rmdir()
    cap = cv2.VideoCapture(0)
    print('Collecting Images for {}'.format(label))
    time.sleep(5)
    if cap.isOpened():
        # current_frame = 0
        for img_num in range(number_imgs):
            ret, frame = cap.read()
            image_name = os.path.join(os.getcwd(),images_path, label + '.' + '{}.jpg'.format(str(uuid.uuid1()))) ## TODO: fix adding images to correct directory
            print(os.getcwd())
            print(image_name)
            cv2.imwrite(image_name, frame)
            cv2.imshow('frame',frame)
            time.sleep(2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
    cv2.destroyAllWindows()



