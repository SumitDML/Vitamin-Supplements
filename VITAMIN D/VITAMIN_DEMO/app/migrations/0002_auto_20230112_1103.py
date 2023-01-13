from __future__ import unicode_literals
from django.db import migrations


def load_app_from_sql():
    import os
    sql_statements = open(os.path.join('app/sql/ZipCodes.sql'), 'r').read()
    return sql_statements


def delete_app_with_sql():
    return 'DELETE from zip_codes;'


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(load_app_from_sql(), delete_app_with_sql()),
    ]
