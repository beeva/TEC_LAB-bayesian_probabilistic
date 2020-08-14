#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Utility to manage experiments.
[X] Create virtual environments - install projects
[] List projects
[] Run notebooks
"""


import argparse
import os

import utils.manage


path_project = os.path.abspath(os.path.join(os.path.dirname(__file__),"."))


def arg_create_venv(args):
    if not os.path.isabs(args.path):
        exp_abs_path = os.path.join(path_project, args.path)
    else:
        exp_abs_path = args.path
    # print(exp_abs_path)
    utils.manage.create_venv(exp_abs_path, os.path.join(path_project,"utils"))


parser = argparse.ArgumentParser()

# Subparsers
subparsers = parser.add_subparsers(
    title='Subcommands',
    description='Functionality',
    # help='additional help'
)

# Create a virtual environment for a experiment
create_venv = subparsers.add_parser(
    'create_venv',
    help="Create a virtual environment to run the experiment"
)
create_venv.add_argument(
    'path',
    help="Path of the experiment, absolute or relative the root of the repo"
)
create_venv.set_defaults(func=arg_create_venv)  # set the default function to hello


if __name__ == '__main__':
    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:  # If any error, print error and help.
        print(e)
        args = parser.parse_args('--help'.split())
        args.func(args)

