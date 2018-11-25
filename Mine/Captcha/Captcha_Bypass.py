Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import cv2.cv as cv
import tesseract
gray = cv.LoadImage('captcha.jpeg', cv.CV_LOAD_IMAGE_GRAYSCALE)
cv.Threshold(gray, gray, 231, 255, cv.CV_THRESH_BINARY)
api = tesseract.TessBaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
api.SetPageSegMode(tesseract.PSM_SINGLE_WORD)
tesseract.SetCvImage(gray,api)
print api.GetUTF8Text()
