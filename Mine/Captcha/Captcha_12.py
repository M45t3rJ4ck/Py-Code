def _generate_img(secret_key):
        """?????????? ??????"""
        image = ImageCaptcha()
        secret_key = str(secret_key)
        generated = image.generate(secret_key)
        return generated.read() 
