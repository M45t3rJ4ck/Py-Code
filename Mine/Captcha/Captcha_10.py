Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def get_captcha():
    """
    ???????
    :return:
    """
    image = ImageCaptcha()
    captcha = gen_random_number_string(4)
    # todo: cache the captcha
    data = image.generate(captcha)
    return Response(data, mimetype='image/jpeg') 
