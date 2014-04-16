#!/bin/bash
#install home brew
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

#install pyqt
brew install qt
brew install sip
brew install pyqt

#setting the path
mkdir -p ~/Library/Python/2.7/lib/python/site-packages
echo '/usr/local/lib/python2.7/site-packages' >> ~/Library/Python/2.7/lib/python/site-packages/homebrew.pth