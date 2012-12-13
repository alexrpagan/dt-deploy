import os
import pystache

#deployment-specific config
META = {
    # absolute path to the location of the virtual env.
    # should be join(absolute-path-to-dt-deploy, 've')
    'VEROOT': '/Users/apagan/Dev/dt-deploy/ve',
    # optional: name of postgres DB user 
    'POSTGRES_USER': 'postgres',
    # optional: command to start postgres
    'POSTGRES_START_CMD': '',
    # user to start redis service.
    'REDIS_USER': 'apagan',
    'REDIS_PORT': '6379',
    # user to start expertsrc uwsgi instance
    'EXPERTSRC_USER': 'apagan',
    # port for expertsrc to listen on
    'EXPERTSRC_PORT': '9999',
    # user to start data tamer uwsgi instance
    'DATA_TAMER_USER': 'apagan',
    # port for data tamer to listen on
    'DATA_TAMER_PORT': '7979',
    # user to start webserver with
    'NGINX_USER': 'apagan',
    # hostname of the server.
    # TODO: make sure that this isn't used to make urls 
    'SERVER_NAME': 'localhost',
    # hostname that will be used to build urls 
    'BASE_URL': '',
    # database info
    'DOIT_DB': 'doit',
    'DOIT_DB_USER': 'doit',
    'DOIT_DB_PASS': '12345',
    'DOIT_DB_PORT': '5432',
    'DOIT_DB_HOST': 'localhost',
    'DOIT_ALT_ROOT': 'apps/datatamer',
    'EXPERTSRC_DB': 'expertsrc',
    'EXPERTSRC_DB_USER': 'expertsrc',
    'EXPERTSRC_DB_PASS': '12345',
    'EXPERTSRC_DB_PORT': '5432',
    'EXPERTSRC_DB_HOST': 'localhost',
    'EXPERTSRC_ALT_ROOT': 'apps/expertsrc',
}

def rewrite_file(filename, aliases):
    new_lines = []
    with open(filename, 'r') as f:
        for line in f:
            new_lines.append(pystache.render(line, aliases))
    with open(filename, 'w') as f:
        f.write(''.join(new_lines))

def rewrite_conf_files(conf_dir_path, aliases):
    for file in os.listdir(conf_dir_path):
        rewrite_file(os.path.join(conf_dir_path, file), aliases)

def main():
    pwd = os.path.abspath(os.path.dirname(__file__))
    conf_dir_path = os.path.abspath(os.path.join(META['VEROOT'], "etcs", "dev"))
    rewrite_conf_files(conf_dir_path, META) 
    rewrite_file(os.path.abspath(os.path.join(META['VEROOT'], "apps/expertsrc/www/expertsrc/settings.py")), META)
    rewrite_file(os.path.abspath(os.path.join(META['VEROOT'], "apps/doit/www/doitweb/settings.py")), META)

if __name__ == "__main__":
    main()
