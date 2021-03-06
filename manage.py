#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Utility to manage experiments.
[X] Create virtual environments - install projects
[] List projects
[] Run notebooks
"""


import argparse
import os

from utils import manage


path_project = os.path.abspath(os.path.join(os.path.dirname(__file__),"."))


def arg_create_venv(args):
    if not os.path.isabs(args.path):
        exp_abs_path = os.path.join(path_project, args.path)
    else:
        exp_abs_path = args.path
    # print(exp_abs_path)
    manage.create_venv(
        exp_abs_path,
        os.path.join(path_project,"utils")
    )


def arg_list_experiments(args):
    experiments = manage.list_experiments(path_project)
    print("Available experiments:")
    for experiment in experiments:
        print("\t{}".format(experiment[len(path_project)+1:]))

    

parser = argparse.ArgumentParser()

# Subparsers
subparsers = parser.add_subparsers(
    title='Subcommands',
    description='Functionality',
    # help='additional help'
)

#
### Create a virtual environment for a experiment
#
create_venv = subparsers.add_parser(
    'create',
    help="Create a virtual environment to run the experiment."
)
create_venv.add_argument(
    'path',
    help="Path of the experiment, absolute or relative to the root of the repo."
)
create_venv.set_defaults(func=arg_create_venv)

#
### List experiments
#
list_experiments = subparsers.add_parser(
    'list',
    help="List available experiments."
)
list_experiments.set_defaults(func=arg_list_experiments)



if __name__ == '__main__':
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        args = parser.parse_args('--help'.split())
        args.func(args)
    except Exception as e:  # If any error, print error and help.
        print(e)

