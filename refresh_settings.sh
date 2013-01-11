#!/bin/bash
set -e
dr=`pwd`

# settings files for services 
cp -r "$dr/conf-files/dev" "$dr/ve/etcs"
if ! [ -e "dr/ve/etc" ]; then
    ln -s "$dr/ve/etcs/dev" "$dr/ve/etc"
fi

# settings files for django applications
cp "$dr/settings-files/expertsrc-settings.py" "$dr/ve/apps/expertsrc/www/expertsrc/settings.py"
cp "$dr/settings-files/doit-settings.py" "$dr/ve/apps/doit/www/doitweb/settings.py"

# replace templated settings files with real values
"$dr/ve/bin/python" "$dr/insert-meta.py"

