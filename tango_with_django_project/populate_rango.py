import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat('python')

    add_page(cat=python_cat,
             title='Official Python Tutorial',
             url='http://docs.python.org/2/tutorial/')
