#!/bin/bash
set -e
dr=`pwd`

cp "$dr/settings-files/expertsrc-settings.py" "$dr/ve/apps/expertsrc/www/expertsrc/settings.py"
cp "$dr/settings-files/doit-settings.py" "$dr/ve/apps/doit/www/doitweb/settings.py"
"$dr/ve/bin/python" "$dr/insert-meta.py"

