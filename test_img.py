import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
from util import util

# save_path = 'results/test'
# if not os.path.exists(save_path):
#     os.makedirs(save_path)

if __name__ == '__main__':
    opt = TestOptions().parse()  # get test options
    # hard-code some parameters for test
    opt.num_threads = 0   # test code only supports num_threads = 0
    opt.batch_size = 1    # test code only supports batch_size = 1
    opt.serial_batches = True  # disable data shuffling; comment this line if results on randomly chosen images are needed.
    opt.no_flip = True    # no flip; comment this line if results on flipped images are needed.
    if not os.path.exists(opt.save_path):
        os.makedirs(opt.save_path)

    dataset = create_dataset(opt)  # create a dataset given opt.dataset_mode and other options
    model = create_model(opt)      # create a model given opt.model and other options
    model.setup(opt)               # regular setup: load and print networks; create schedulers

    if opt.eval:
        model.eval()
    for i, data in enumerate(dataset):
        if i >= opt.num_test:  # only apply our model to opt.num_test images.
            break
        model.set_input(data)  # unpack data from data loader
        model.test()           # run inference
        visuals = model.get_current_visuals()  # get image results

        im = util.tensor2im(visuals['fake_A'])
        img_path = model.get_image_paths()  # get image paths
        # print(img_path)
        img_list = img_path[0].split("\\")
        save_path = os.path.join(opt.save_path, img_list[-1])
        util.save_image(im, save_path, aspect_ratio=1.0)
        if i % 5 == 0:  # save images to an HTML file
            print('processing (%04d)-th image... %s' % (i, img_path))

