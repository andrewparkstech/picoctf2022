#!/bin/bash

cat Financial_Report_for_ABC_Labs.txt | grep -oE "picoCTF{.*?}" --color=none
