import os

from split_settings.tools import include

include(
    'base.py',
    'database.py',
)

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'local')
if ENVIRONMENT == 'production':
    include('production.py')
else:
    include('local.py')
