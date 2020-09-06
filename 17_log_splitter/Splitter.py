import re
import os
import sys
import argparse
import threading


class Splitter():
    def __init__(self):
        self.application = None
        self.level = None
        self.path_original_log = None
        self.set_log_file()

    def set_level(self, level=None):
        if level:
            self.level = level
        else:
            self.level = input('type log level: ')

    def set_app(self, app=None):
        if app:
            self.app = app
        else:
            self.app = input('type app name: ')

    def set_log_file(self, file=None):
        if file:
            self.path_original_log = file
        else:
            self.path_original_log = input(
                'drop original log file into terminal: ')

    def split_file(self, app=None, level=None):
        buf = []
        lines = []
        with open(self.path_original_log, 'r') as log:
            lines = log.readlines()
        for line in lines:
            if re.search(r'^\[', line):  # regexp for app
                with open('{}.log'.format(app), 'a') as out_app:
                    out_app.write(line)
            if re.search(r'^\[', line):  # regexp for level
                with open('{}.log'.format(level), 'a') as out_level:
                    out_level.write(line)
        return None


def init_argparser():
    parser = argparse.ArgumentParser()
    # e.g. [ERROR]/[ERR]/[E]/etc.
    parser.add_argument('-lvl', metavar='LEVEL', type=str, required=False)
    # e.g. [LOGWRITER]/[LOGGER]/[LOG]/etc.
    parser.add_argument('-app', metavar='APP', type=str, required=False)
    return parser


def main():
    argparser = init_argparser()
    args.parse_args()
    split = Splitter()
    split.set_level(args['level']) if args['level'] else split.set_level()
    split.set_app(args['app']) if args['app'] else split.set_app()
    split.set_log_file(args['file']) if args['file'] else split.set_log_file()
    split.split_file()


if __name__ == '__main__':
    main()
sshpass - p q7KtsXLQzkhAj ssh zodiac@30.255.240.238 pwreg forceset DGroup 209
