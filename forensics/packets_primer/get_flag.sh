#!/bin/bash

strings network-dump.flag.pcap | sed 's/ //g' | grep "pico" --color=none
