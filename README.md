# certifier_py

## How to install

```shell
sudo pip3 install virtualenv
virtualenv .venv
pip3 install -m requirements.txt
```

## setup

```shell
pip3 install -r requirements.txt
./setup.py install
```

or cleaning up first

```shell
./setup.py clean --all install
```

## run

```shell
certifier <command>
```

## testing

```shell
python3 -m unittest src/**/test_*.py
```
