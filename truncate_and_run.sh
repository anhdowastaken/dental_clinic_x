rm -rf db.sqlite3 dental_clinic_x/migrations/
python3 manage.py makemigrations dental_clinic_x
python3 manage.py sqlmigrate dental_clinic_x 0001
python3 manage.py migrate
python3 ./sqlite3_script.py
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000

