#!/bin/bash

python patchme.flag.py | grep -oE "picoCTF{.*?}" --color=none
