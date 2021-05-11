import os
import os.path as osp

import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--coco_src',
        type=str,
        help='source folder of COCO hand dataset training or val cohort.')
    parser.add_argument(
        '--dst', '-d', type=str, help='destination txt file path.')
    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    src_folder = args.src
    dst_path = args.dst

    fp = open(dst_path, 'w')
    for item in os.listdir(src_folder):
        fp.write(osp.splitext(item)[0] + '\n')


if __name__ == '__main__':
    main()
