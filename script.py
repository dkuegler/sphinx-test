import argparse


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("test")
    sp = parser.add_subparsers(title="subparsers")
    sp.add_parser("sub-mode").add_argument("test")

    return parser


if __name__ == "__main__":
    make_parser().parse_args()
