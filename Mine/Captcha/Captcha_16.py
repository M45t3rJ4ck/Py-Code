def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p",
                        "--path",
                        required=False,
                        help="path to store generated images")
    parser.add_argument("-n",
                        "--number",
                        required=True,
                        help="number of images generated")
    producer = ImageCaptcha(width=config['image_width'],
                            height=config['image_height'],
                            font_sizes=[40])
    args = vars(parser.parse_args())
    if "path" not in args:
        path = config['images_path']
    else:
        path = args['path']
    if not os.path.exists(path):
        os.makedirs(path)
    print("Starting generating %d images in %s" % (int(args['number']), path))
    for i in range(int(args['number'])):
        number_to_write = "".join([random.choice(string.digits) for _ in range(4)])
        producer.write(number_to_write, os.path.join(path, str(i)+"_"+number_to_write+".png"))
    print("images generated!")
    print("-" * 30)

    print("Staring convert tfrecords of these generated images!")
    generate_tfrecords(path)
    print("tfrecords generated!") 
