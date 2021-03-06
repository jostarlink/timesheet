# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from timesheet.configuration import init_config, config
__author__ = 'vahid'
__version__ = '0.9.7'


def entrypoint():

    # initializing configuration
    init_config()

    # initializing models if not initialized yet
    from timesheet import models
    models.init()

    # Preparing cli arguments
    from timesheet import cli
    args = cli.parse_ars()

    # Dispatch and execute the command
    if hasattr(args, 'command_class'):
        args.command_class(args).do_job()

    sys.exit(0)
