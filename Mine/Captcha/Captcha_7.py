Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def gen_random_captcha_image():
    image = ImageCaptcha(width=config.IMAGE_WIDTH, height=config.IMAGE_HEIGHT, font_sizes=[config.FONT_SIZE])

    text = __gen_random_captcha_text(size=config.MAX_CAPTCHA)
    captcha = image.generate(text)
    captcha_image = Image.open(captcha)
    captcha_source = np.array(captcha_image)
    return text, captcha_source


# always gen the require image height ,and width image 
