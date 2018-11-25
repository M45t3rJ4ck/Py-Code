Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def gen_captcha_text_and_image(width=CAPTCHA_WIDTH, height=CAPTCHA_HEIGHT,save=None):
    '''
    ???????
    :param width:
    :param height:
    :param save:
    :return: np??
    '''
    image = ImageCaptcha(width=width, height=height)
    # ?????
    captcha_text = random_captcha_text()
    captcha = image.generate(captcha_text)
    # ??
    if save: image.write(captcha_text, captcha_text + '.jpg')
    captcha_image = Image.open(captcha)
    # ???np??
    captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image 
