### import packages

import torch
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st

### read the model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5m6.pt', force_reload=True)

### Use the model
# img = cv2.imread('2.jpg')
# img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# results = model(img_2)
# img_3 = np.squeeze(results.render())
# st.image(img_3)
# plt.imshow(img_3)
# plt.savefig('res-2.jpg')

### streamlit app

st.header('Detect play , challenge or throwin events from soccer videos')

uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mpeg","jpg","png"])
if uploaded_file is not None:

    # print(uploaded_file.name)
    # img=[]
    # for ret, frame in uploaded_file:
    #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #     results = model(frame)
    #     img.append(np.squeeze(results.render()))
    # # video_file = open(uploaded_file.name, 'rb')
    # video_bytes = img.read()
    #
    # st.video(video_bytes)
    # # return uploaded_file
    # img_2 = cv2.cvtColor(uploaded_file, cv2.COLOR_BGR2RGB)
    # results = model(img_2)
    # img_3 = np.squeeze(results.render())
    plt.imshow(img_3)
    plt.savefig(f'res-{uploaded_file.name}')
    st.image(f'res-{uploaded_file.name}')


print('Done ...')
