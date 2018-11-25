def gen_random_captcha_image():
    image = ImageCaptcha(width=config.IMAGE_WIDTH, height=config.IMAGE_HEIGHT,font_sizes=[config.FONT_SIZE])

    text = __gen_random_captcha_text(size=config.MAX_CAPTCHA)
    captcha = image.generate(text)
    captcha_image = Image.open(captcha)
    captcha_source = np.array(captcha_image)
    return text, captcha_source


# always gen the require image height ,and width image 
