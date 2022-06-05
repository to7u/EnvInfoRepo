#! /bin/bash

# python install 3.8.6
pyenv install 3.8.6
pyenv rehash
pyenv global 3.8.6

# python module install
pip install --upgrade pip setuptools
pip install pillow netifaces requests bs4 lxml

# ruby install 2.5.7
rbenv install 2.5.7
rbenv rehash
rbenv global 2.5.7

# php install 7.2.22
phpenv install 7.2.22
phpenv rehash
phpenv global 7.2.22
