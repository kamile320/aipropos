#!/bin/bash

# Building .deb installer
version="1.2"
maindir=$(pwd)
cd ~
dir=$(pwd)
mkdir aipropos_tmp
cd aipropos_tmp
mkdir -p DEBIAN
mkdir -p usr/bin
mkdir -p usr/share/aipropos

# Main
cp $maindir/build/aipropos usr/bin/aipropos
cp $maindir/aipropos.py usr/share/aipropos/aipropos.py
cp $maindir/install.sh usr/share/aipropos/install.sh

# DEBIAN/control
cp $maindir/build/control DEBIAN/control

# Permissions
cd ..
chmod -R 775 aipropos_tmp/*

# Building .deb
dpkg-deb --build aipropos_tmp $dir/aipropos_v$version.deb

# Cleanup
rm -rf aipropos_tmp
echo "aipropos_v$version.deb has been created in $dir"
cd $maindir