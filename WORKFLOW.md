python -m pytest  -k test_unit -q   QUIET


python -m pytest  -k test_cat -vs
python -m pytest  -k test_prod -vs
python -m pytest  -k test_sea -k test_at -vs
python -m pytest  -vs 'all pass' in 06

[alembic] - ensure this is here as it does not seem to find devdb section
script_location = migrations
prepend_sys_path = .
version_path_separator = os
sqlalchemy.url =

remove all containers
clear all migrations
docker-compose up -d
run `alembic -n devdb revision --autogenerate -m "initial"` # gets sqlalchemy.url
run `alembic upgrade head` - this will populate 
run `python -m pytest  -vs` which will create test-db, add tables and run tests which will pass/ 