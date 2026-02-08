set -o errexit

pip install --no-cache-dir -r requirements.txt

python manage.py collectstatic --noinput 

python manage.py migrate

python manage.py create_user_groups

if [ "$CREATE_SUPERUSER" = "true" ]; then
    python manage.py createsuperuser --noinput
fi
