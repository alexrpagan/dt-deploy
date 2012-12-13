dt-deploy
=========

Deployment scripts for Data-Tamer.

Setup
----------

0. Make sure that you have working installations of gcc, gmake, Postgres 9.1+, Python 2.5+ and plpython. Also make sure that header files for python and postgres are installed (e.g. libpq-dev, python-dev in Ubuntu).

1. Clone expertsrc and doit (data-tamer core).

    cd $DT/github
    git clone https://github.com/alexrpagan/expertsrc.git
    git clone https://github.com/alexrpagan/doit.git
    cd ..

2. Install python packages and binaries.

    $DT/bootstrap.sh

3. Create databases.

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

4. Modify site-specific settings. These are found in the META dict in insert-meta.py. 

5. Install site-specific settings.

    $DT/reset_settings.sh

6. Initialize data tamer database

    . $DT/ve/apps/doit/init "doit -U doit"

7. Initialize expertsrc database

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

8. Start services

    supervisord -c $DT/ve/etc/supervisord
    # check status...
    supervisorctl

