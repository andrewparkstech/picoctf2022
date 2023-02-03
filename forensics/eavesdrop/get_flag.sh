#!/bin/bash

openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123 && cat file.txt
