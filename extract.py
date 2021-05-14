import argparse
import json
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str)
    parser.add_argument('--dst', type=str)

    return parser.parse_args()


def main():
    args = parse_args()
    src_path = args.src
    dst_path = args.dst

    collect = []
    json_pointer = open(src_path, 'r')
    lines = json_pointer.readlines()[1:]
    for line in lines:
        temp = json.loads(line)
        if temp['mode'] == 'train':
            collect.append(temp["loss"])

    np.save(dst_path, np.array(collect))


if __name__ == '__main__':
    main()
