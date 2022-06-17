#!/bin/bash

echo "picoCTF{$(cat encoded.txt | base64 -d)}"
