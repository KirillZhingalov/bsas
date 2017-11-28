### Vizualizer for BSA-3 data

How to use:
1) make venv
```
python3 -m venv bsa_venv
source bsa_venv/bin/activate
```

2) clone repo
```
git clone
```

3) install necessary modules
```
pip install -r requirements
```

3.1) Only first time
```
python manage.py migrate
```

4) create ssh-tunnel to db
```
ssh -p 22023 -fNqv -L 5556:postgres-prao:5432 student01@217.26.24.31
```

5) start
```
python manage.py runserver
```
