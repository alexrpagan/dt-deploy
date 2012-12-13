#!/bin/bash
#
# Usage: ./bootstrap.sh
#
# This script will create a new Python virtualenv at ./ve
# and install all of the binaries and python libraries.
#
# Note that this version of virtualenv requires Python 2.5
# or greater.
#
# run ./reset_settings.sh to fill in templated conf files
# with site-specific settings. 

set -e
dr=`pwd`
if [ -d "$dr/ve" ]
    then
        rm -rf "$dr/ve"
fi

python "$dr/virtualenv.py" \
    --extra-search-dir="$dr/requirements/virtualenv-support" \
    --never-download \
    "$dr/ve"

"$dr/ve/bin/pip" install \
    -E "$dr/ve" \
    --index-url='' \
    --requirement="$dr/pylibs.txt"

python "$dr/virtualenv.py" --relocatable "$dr/ve"

declare -a new_dirs=(log pid apps etcs tmp sock pkg)
for dir in "${new_dirs[@]}"
do
    if ! [ -d "$dir" ]
        then
            mkdir "$dr/ve/$dir"
    fi
done

cp -r "$dr/conf-files/dev" "$dr/ve/etcs"
ln -s "$dr/ve/etcs/dev" "$dr/ve/etc"

nginx_pkg='nginx-1.2.3'
tar -xvf "$dr/requirements/lib-tarballs/$nginx_pkg.tar.gz" 
cd "$dr/$nginx_pkg"
./configure --without-http_rewrite_module --without-http_gzip_module
make
cp objs/nginx "$dr/ve/bin/nginx" 
rm -rf "$dr/$nginx_pkg"
cd "$dr"

redis_pkg='redis-2.4.17'
tar -xvf "$dr/requirements/lib-tarballs/$redis_pkg.tar.gz"
cd "$dr/$redis_pkg"
make PREFIX="$dr/ve" install
rm -rf "$dr/$redis_pkg"
cd "$dr"

glpk_pkg='glpk-4.35'
tar -xvf "$dr/requirements/lib-tarballs/$glpk_pkg.tar.gz"
cd "$dr/$glpk_pkg"
./configure --prefix="$dr/ve"
make
make install
rm -rf "$dr/$glpk_pkg"
cd "$dr"

cp -r "$dr/github/expertsrc" "$dr/ve/apps/expertsrc"
cp -r "$dr/github/doit" "$dr/ve/apps/doit"

