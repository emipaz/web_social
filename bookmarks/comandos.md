# Creacion del projecto

```bash
django-admin startproject bookmarks .

python manage.py startapp account

python manage.py migrate

python manage.py createsuperuser
```


## instalacion de pillow

```bash
python -m pip install pillow
```	

```powershell

(env_book) PS E:\Projectos-Django\web_social\bookmarks> pip list
WARNING: Ignoring invalid distribution -ip (e:\projectos-django\web_social\env_book\lib\site-packages)
Package           Version
----------------- -------
asgiref           3.7.2
Django            4.2
pillow            10.2.0
pip               24.0
setuptools        58.1.0
sqlparse          0.4.4
typing_extensions 4.10.0
tzdata            2024.1
wheel             0.42.0
(env_book) PS E:\Projectos-Django\web_social\bookmarks> py .\manage.py check
System check identified no issues (0 silenced).
(env_book) PS E:\Projectos-Django\web_social\bookmarks> py .\manage.py makemigrations
Migrations for 'account':
  account\migrations\0001_initial.py
    - Create model Profile
(env_book) PS E:\Projectos-Django\web_social\bookmarks> py .\manage.py sqlmigrate account 0001
BEGIN;
--
-- Create model Profile
--
CREATE TABLE "account_profile" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "fecha_nacimiento" date NULL, "foto" varchar(100) NOT NULL, "usuario_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
COMMIT;
(env_book) PS E:\Projectos-Django\web_social\bookmarks> py .\manage.py migrate
Operations to perform:
  Apply all migrations: account, admin, auth, contenttypes, sessions
Running migrations:
  Applying account.0001_initial... OK
(env_book) PS E:\Projectos-Django\web_social\bookmarks>

```	

## importacion de settings del projecto en consola

```powershell
(env_book) PS E:\Projectos-Django\web_social\bookmarks> py .\manage.py shell
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.conf import settings
>>> settings.BASE_DIR
WindowsPath('E:/Projectos-Django/web_social/bookmarks')
```	
