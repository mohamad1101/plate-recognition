# ALL needed parameters set in this file.
# change this parameters as you want 

import numpy as np
import os

# RTSP camera url
# rtsp://192.168.1.240:554/H264?ch=1&subtype=1&proto=Onvif
# rtsp://admin:123456@192.168.226.202:550/mode=real&idc=1&ids=1
url = 'http://192.168.1.5:8080/video'
# there is two types of kernels for using in the erosion phase
thin_kernel = np.ones((3, 3), np.uint8)
wide_kernel = np.ones((5, 5), np.uint8)

# min amd max of pixel in a contour for remove small and big contours
minimum_contour_size = 1000
maximum_contour_size = 25000

# pyteseract installed path
pyteseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# persian numbers
persian_numbers = {
    "۰": 0,
    "۱": 1,
    "۲": 2,
    "۳": 3,
    "۴": 4,
    "۵": 5,
    "۶": 6,
    "۷": 7,
    "۸": 8,
    "۹": 9
}

# minimum and maximum number of persian numbers for accept as a plate
minimum_persian_numbers_count = 4
maximum_persian_numbers_count = 8

# db variables
db_path = os.path.join("C:\\Users\\mohamad\\Desktop\\plate\\plate-recognition-main\\src\\db", "iCCard.mdb")
db_pass = "168168"

# log size
log_file_size = 50 * 1025 * 1024
