import argparse
import shutil


def copy_file(args):
    shutil.copy(args.src, args.dst)