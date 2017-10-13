#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Porter, Richard B
# Copyright (c) 2017 Porter, Richard B
#
# License: MIT
#

"""This module exports the Drupalcs plugin class."""

from SublimeLinter.lint import Linter, util


class Drupalcs(Linter):
    """Provides an interface to drupalcs."""

    syntax = ('php', 'html', 'html 5')
    regex = (
        r'.*line="(?P<line>\d+)" '
        r'column="(?P<col>\d+)" '
        r'severity="(?:(?P<error>error)|(?P<warning>warning))" '
        r'message="(?P<message>.*)" source'
    )
    executable = 'phpcs'
    defaults = {
        '--standard=': 'Drupal,DrupalPractice',
    }
    inline_overrides = ('standard')
    tempfile_suffix = 'php'

    def cmd(self):
        """Read cmd from inline settings."""
        settings = Linter.get_view_settings(self)

        if 'cmd' in settings:
            command = [settings.get('cmd')]
        else:
            command = [self.executable_path]

        command.append('--report=checkstyle')

        return command
