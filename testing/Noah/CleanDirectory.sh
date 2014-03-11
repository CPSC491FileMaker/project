#!/bin/bash

PYC=$(ls | grep .pyc)
TEMPS=$(ls | grep .*~)
SWP=$(ls -a | grep .swp)

if [ ! -z "$PYC" ]; then
    rm -rf *.pyc
fi
if [ ! -z "$TEMPS" ]; then
    rm -rf *.*~
fi
if [ ! -z "$SWP" ]; then
    rm -rf .*.swp
fi
