def gen_captcha_text_and_image(fileDir = 'E:/work/captcha/susongwuyou/train/'):
    # image = ImageCaptcha()
    # captcha_text = random_captcha_text()
    # captcha_text = ''.join(captcha_text)
    # captcha = image.generate(captcha_text)
    # captcha_image = Image.open(captcha)
    # captcha_image = np.array(captcha_image)
    # fileDir = 'E:/work/captcha/susongwuyou/train/'
    # fileDir = 'D:/work/captcha/panjueshu/test/'
    all_image = os.listdir(fileDir)
    random_file = random.randint(0, len(all_image)-1)
    base = os.path.basename(fileDir + all_image[random_file])
    name = os.path.splitext(base)[0]
    image = Image.open(fileDir + all_image[random_file])
    image = np.array(image)
    return name, image



##????????? 
