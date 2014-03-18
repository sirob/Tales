#-*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True  #a to sploh rabiš, če ni logina?
SECRET_KEY = 'geslo'

#pagination
STORIES_PER_PAGE = 10