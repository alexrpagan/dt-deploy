#!/bin/bash
set -e
dr=`pwd`
if [ -d "$dr/ve" ]
    then
        rm -r "$dr/ve"
fi

python "$dr/scripts/virtualenv.py" \
    --extra-search-dir="$dr/requirements/virtualenv-support" \
    --never-download \
    "$dr/ve"

"$dr/ve/bin/pip" install \
    -E "$dr/ve" \
    --index-url='' \
    --requirement="$dr/pylibs.txt"

python "$dr/scripts/virtualenv.py" --relocatable "$dr/ve"

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

expertsrc_pkg='expertsrc-master'
unzip -d "$dr/github/" "$dr/github/$expertsrc_pkg.zip"
mv "$dr/github/$expertsrc_pkg" "$dr/ve/apps/expertsrc"
cp "$dr/settings-files/expertsrc-settings.py" "$dr/ve/apps/expertsrc/www/expertsrc/settings.py"

doit_pkg='doit-master'
unzip -d "$dr/github" "$dr/github/$doit_pkg.zip" 
mv "$dr/github/$doit_pkg" "$dr/ve/apps/doit"
cp "$dr/settings-files/doit-settings.py" "$dr/ve/apps/doit/www/doitweb/settings.py"

cd "$dr/ve"
./bin/python "$dr/scripts/insert-meta.py" || exit
cd "$dr"
