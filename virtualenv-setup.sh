# global
# Created by: Christopher Bess
# It is recomm. not to run this script using sudo, it is used as needed.
#
# Run this script from this `setup` directory.
#
# user$: sh ./virtualenv-setup.sh

echo "Setting up virtualenv and pip"
sudo easy_install pip
sudo pip install virtualenv

# adjust permission (allow it to be executed)
chmod +x ./main.py

# if on a Mac exec below line (maybe)
# ARCHFLAGS="-arch i386 -arch x86_64"

# setup environment
virtualenv ./json_env --distribute --no-site-packages
source ./json_env/bin/activate

echo "Installing dependencies"
./json_env/bin/pip install -r requirements.txt

echo "Done, install finished"