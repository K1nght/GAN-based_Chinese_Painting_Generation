import os
import glob
from PIL import Image


def load_resized_img(path):
    return Image.open(path).convert('RGB').resize((256, 256))


def load_crop_img(path, x1, y1, x2, y2):
    return Image.open(path).convert('RGB').crop((x1, y1, x2, y2))


def process(photo_dir, output_dir):
    savedir = output_dir
    os.makedirs(savedir, exist_ok=True)
    print("Directory structure prepared at %s" % output_dir)

    photo_expr = photo_dir + "/*.jpg"
    photo_paths = glob.glob(photo_expr)
    photo_paths = sorted(photo_paths)

    print('The size of photo is %d' % len(photo_paths))
    for i, photo_path in enumerate(photo_paths):
        photo = Image.open(photo_path).convert('RGB')
        img_name = photo_path.split("\\")[-1]
        x, y = photo.size
        if x > y:
            photo2 = photo.crop(((x - y) // 2, 0, (x + y) // 2, y))
            ph = photo2.resize((256, 256))
            savepath = os.path.join(savedir, img_name)
            ph.save(savepath, format='JPEG', subsampling=0, quality=100)
        else:
            photo2 = photo.crop((0, (y - x) // 2, x, (y + x) // 2))
            ph = photo2.resize((256, 256))
            savepath = os.path.join(savedir, img_name)
            ph.save(savepath, format='JPEG', subsampling=0, quality=100)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--photo_dir', type=str, required=True,
                        help='Path to the photo directory.')
    parser.add_argument('--output_dir', type=str, required=True,
                        default='./datasets/chinesePainting',
                        help='Directory the output images will be written to.')
    opt = parser.parse_args()

    print('Preparing %s Dataset' % opt.photo_dir)
    process(opt.photo_dir, opt.output_dir)

    print('Done')
