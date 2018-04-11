Ideate - the API driven Idea Management platform
====================================

Quick start
===========

Run Ideate::

    - virtualenv ideate
    - cd ideate
    - git clone git@github.com:MTN-Group/ideate.git
    - source bin/activate
    - pip install djangorestframework
    - pip install markdown       # Markdown support for the browsable API.
    - pip install django-filter  # Filtering support
    - python manage.py migrate
    - python manage.py runserver

Browse to `http://localhost:8000/ideas/api/` to view ideate API browser.
