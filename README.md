dt-deploy
=========

Deployment scripts for Data-Tamer.

Setup
----------

Make sure that you have working installations of gcc, gmake, Postgres 9.1+, Python 2.5+ and plpython. Also make sure that header files for python and postgres are installed (e.g. libpq-dev, python-dev in Ubuntu).

Clone expertsrc and doit (data-tamer core).

    cd $DT/github
    git clone https://github.com/alexrpagan/expertsrc.git
    git clone https://github.com/alexrpagan/doit.git

Install python packages and binaries.

    . $DT/bootstrap.sh

Create databases.

    createuser -s expertsrc
    createuser -s doit
    psql template1
    CREATE LANGUAGE plpythonu;
    -- set user passwords...
    \q
    createdb expertsrc -O expertsrc
    createdb doit -O doit
    psql doit -U doit
    CREATE SCHEMA doit;
    ALTER USER doit SET search_path to doit;
    \q 

Modify site-specific settings. These are found in the META dict in insert-meta.py. 

Install site-specific settings.

    . $DT/reset_settings.sh

Initialize data tamer database

    . $DT/ve/apps/doit/init "doit -U doit"

Initialize expertsrc database

    # activate virtualenv
    . $DT/ve/bin/activate
    cd $DT/ve/apps/expertsrc
    . ./sql/init "expertsrc -U expertsrc"
    python ./www/expertsrc/manage.py syncdb
    # follow instructions...
    python ./www/expertsrc/manage.py migrate ui
    # create fake crowd workers
    python ./www/expertsrc/manage.py create_users
    # reset market
    python ./www/expertsrc/manage.py reset_nr_questions

Start services

    supervisord -c $DT/ve/etc/supervisord
    # check status...
    supervisorctl

