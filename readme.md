# django_template

## 環境セットアップ
``` shell
# 開発環境用Docker立ち上げ
$ ./rename_project.py <new project name> <new port for development>
$ docker-compose -p <prefix> build && docker-compose -p <prefix> up
# access 'http://localhost:<new port for development>'

# localでも使うのでvirtualenv作成
$ mkvirtualenv --no-site-packages -p /usr/bin/python3.6 <new project name>
$ pip install -r requirements.txt
```
