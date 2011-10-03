#!/usr/bin/env python

# Stub for the CLI

import core
from formats import Formats
import sys

core.convert(sys.argv[1], sys.argv[2], Formats.get(sys.argv[3]) )
