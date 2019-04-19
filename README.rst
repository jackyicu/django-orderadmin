=====
OrderAdmin
=====

OrderAdmin is a simple Django app to conduct order admin and tracking. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "orderadmin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'orderadmin',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('orderadmin/', include('orderadmin.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to start to adminnitrate your orders (you'll need the Admin app enabled).
