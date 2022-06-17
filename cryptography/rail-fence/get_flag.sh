#!/bin/bash

python rail_fence.py | grep -oE "picoCTF{.*?}" --color=none
