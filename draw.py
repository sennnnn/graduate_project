import numpy as np
import matplotlib.pyplot as plt

# hand_gener = np.load('yolov3_hand.npy')
# hand_custo = np.load('hand_cnn.npy')

# x = [x*50 for x in range(1, hand_gener.shape[0] + 1)]

# plt.plot(x, hand_gener, color='#A162D0', label='Yolov3-hand')
# plt.plot(x, hand_custo, color='#02FFC4', label='Hand-CNN')

face_gener = np.load('yolov3_face.npy')
face_custo = np.load('retinaface.npy')

x = [x*50 for x in range(1, face_gener.shape[0] + 1)]

plt.plot(x, face_gener, color='#5F86CD', label='Yolov3-Face')
plt.plot(x, face_custo, color='#02FFFF', label='RetinaFace')

plt.legend()
plt.grid()
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
plt.show()