FROM php:7.4-apache
RUN apt-get update && apt-get install -y libonig-dev && \
  docker-php-ext-install pdo_mysql mysqli mbstring

RUN apt-get -y install vim sudo less

RUN echo "\n\
alias rm='rm -i'\n\
alias ll='ls -l --color'\n\
alias la='ls -la --color'\n\
" >> ~/.bashrc

COPY .vimrc ~/
