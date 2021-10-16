# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function
import os
# Pour acceder à prompt_toolkit
import sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
#-- 

from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.validation import Validator, ValidationError

from .utils import print_json, format_json


__version__ = '1.0.2'


def here(p):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class PromptParameterException(ValueError):
    def __init__(self, message, errors=None):

        # Call the base class constructor with the parameters it needs
        super(PromptParameterException, self).__init__(
            'You must provide a `%s` value' % message, errors)

from .prompt import prompt
from .separator import Separator
from .prompts.common import default_style
