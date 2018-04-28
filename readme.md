Wagtail Space
=============

Wagtail Space is a Wagtail event hosted by Four Digits in Arnhem, The Netherlands.

We like others to organise Wagtail Space events as well.

If you like to organise a Wagtail meet up, sprint or conference you may use the Wagtail Space name, graphics and website!

What we propose:

    - Name your Wagtail event: 'Wagtail Space [CityName]'. Eg: 'Wagtail Space Philadelphia'.
    - Notify Four Digits and get a subdomain (philadelphia.wagtail.space)
    - We list your event on [wagtail.space](https://wagtail.space)

To be eligible for a subdomain we require you to:
    - Adhere to the naming scheme
    - Provide hosting yourself (supply an ip address)
    - Use an SSL-certificate
    - Notify Wagtail Core team of your event plans


Install
-------

Clone this repo:

    git clone git@github.com:fourdigits/wagtailspace.git


Create an environment and install Python packages:

    virtualenv env -p python3
    source env/bin/activate
    pip install -r requirements.txt


Configure your database. Copy and edit local.py. (secret key and database credentials).

    cp wagtailspace/settings/local.py.example wagtailspace/settings/local.py
    vi wagtailspace/settings/local.py


Make migrations, create a user and run the development server:

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver


Frontend
--------

    yarn
    yarn start


Deploy
------

Build the frontend locally and copy the results to the server:

    git pull origin master
    yarn build
    scp wagtailspace/static user@server.tld:/path/to/wagtailspace/wagtailspace
    scp config-prd-stats.json user@server.tld:/path/to/wagtailspace


On the server:

    pip install -r requirements/prd.txt
    python manage.py collectstatic
    python manage.py migrate


Restart.
