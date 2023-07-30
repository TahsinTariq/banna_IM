__version__ = 'dev'
from PIL import Image
import cv2
import requests
from io import BytesIO
import numpy as np
import altair as alt
import pandas as pd
import PIL.ImageOps
import base64, io, IPython
from skimage import data, img_as_float
from skimage import exposure
alt.data_transformers.disable_max_rows()
def get_image_pd(image):
    output = io.BytesIO()    
    image.save(output, format='JPEG')
    encoded_string = "data:image/jpeg;base64,"+base64.b64encode(output.getvalue()).decode()
    x = [0]
    y = [0]
    source = pd.DataFrame({"x": x, "y": y, "img": [encoded_string]})
    return source


# def get_image_plot(image, title=''):
#     source = get_image_pd(image)
#     return alt.Chart(source, title = title).mark_image(width=800, height=600).encode(x='x', y='y', url='img')

def show_im(image, title=''):
    source = get_image_pd(image)
    return alt.Chart(source, title = title).mark_image(width=800, height=650).encode(x=alt.X("x",
                                                                                             scale = alt.Scale(nice=False), 
                                                                                             axis=alt.Axis(title='', ticks=False, domain=False )), 
                                                                                     y=alt.Y("y",
                                                                                             scale = alt.Scale(nice=False), 
                                                                                             axis=alt.Axis(title='', ticks=False, domain=False )),  
                                                                                     url='img')


import skimage.util as util
def add_noise(im, noise_type, percentage=0.3):
    title = ""
    nimg = util.random_noise(np.array(im), mode=noise_type)*255
    return show_im(Image.fromarray(np.array(nimg, dtype = np.uint8)), title = title)

def median_f(size):
    return show_im(Image.fromarray(cv2.medianBlur(np.array(im),size)))
