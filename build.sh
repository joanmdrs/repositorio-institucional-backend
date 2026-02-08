set -o errexit

pip install --no-cache-dir -r requirements.txt

python manage.py collectstatic --noinput 

python manage.py migrate

python manage.py create_user_groups

python manage.py create_superuser_if_not_exists

