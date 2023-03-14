FROM php:fpm

COPY php.ini $PHP_INI_DIR/conf.d/

# 安裝 php extensions 的神器，請務必一試！
# https://github.com/mlocati/docker-php-extension-installer
COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/bin/

RUN install-php-extensions redis mysqli xdebug

RUN apt-get update

RUN apt-get install -y libpq-dev \
  && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
   && docker-php-ext-install pdo pdo_pgsql pgsql