#!/bin/bash

echo "202752" | nc saturn.picoctf.net 52279 | grep -oE "picoCTF{.*}"

