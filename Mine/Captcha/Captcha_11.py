def __init__(self, count, batch_size, num_label, init_states):
        super(OCRIter, self).__init__()
        self.captcha = ImageCaptcha(fonts=['./data/Xerox.ttf'])
        self.batch_size = batch_size
        self.count = count
        self.num_label = num_label
        self.init_states = init_states
        self.init_state_arrays = [mx.nd.zeros(x[1]) for x in init_states]
        self.provide_data = [('data', (batch_size, 2400))] + init_states
        self.provide_label = [('label', (self.batch_size, 4))] 
