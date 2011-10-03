#!/usr/bin/python

# Stub for the CLI

import core
import formats
import sys

core.convert(sys.argv[1], sys.argv[2], formats.WAV)
