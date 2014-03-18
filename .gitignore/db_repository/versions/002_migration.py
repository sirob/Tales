from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
story = Table('story', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String),
    Column('body', Text),
    Column('location', String),
    Column('timestamp', DateTime),
    Column('pseudonym', String),
    Column('email', String),
)

story = Table('story', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=90)),
    Column('body', Text(length=1800)),
    Column('location', String(length=64)),
    Column('time', String(length=90)),
    Column('timestamp', DateTime),
    Column('pseudonym', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['story'].columns['email'].drop()
    post_meta.tables['story'].columns['time'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['story'].columns['email'].create()
    post_meta.tables['story'].columns['time'].drop()
