#!/bin/bash

python getflag.py | grep -oE "picoCTF{.*}" --color=none
