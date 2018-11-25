Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def gen(gen_dir, total_size, chars_num):
  if not os.path.exists(gen_dir):
    os.makedirs(gen_dir)
  image = ImageCaptcha(width=IMAGE_WIDTH, height=IMAGE_HEIGHT,font_sizes=[40])
  # must be subset of config.CHAR_SETS
  char_sets = 'ABCDEFGHIJKLMNPQRSTUVWXYZ'
  for i in xrange(total_size):
    label = ''.join(random.sample(char_sets, chars_num))
    image.write(label, os.path.join(gen_dir, label+'_num'+str(i)+'.png')) 
