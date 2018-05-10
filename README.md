```
     _/_/_/                    _/                                     
    _/    _/    _/_/      _/_/_/    _/_/      _/_/    _/_/_/  _/_/    
   _/_/_/    _/_/_/_/  _/    _/  _/_/_/_/  _/_/_/_/  _/    _/    _/   
  _/    _/  _/        _/    _/  _/        _/        _/    _/    _/    
 _/    _/    _/_/_/    _/_/_/    _/_/_/    _/_/_/  _/    _/    _/     
```

Replicape is an attachment for BeagleBone to control control 3D printers and CNC machines, such as routers, lathes and mills.

Redeem is its firmware; it accepts g-codes and translates them into coordinates for your device.

## Software features

- Acceleration with corner speed prediction
- Printer settings loaded from files
- Controllable via OctoPrint, ethernet, USB or MagnaScreen
- Written in python for extensibility
- Optimized for BeagleBone's secondary processing units
- Extendable plugin architecture

## Documentation

[intelligent-agent.github.io](http://intelligent-agent.github.io)

## Installation options

### BeagleBone image

Umikaze (based on ubuntu 16.03.04)

### Debian package

```
wget -O - http://kamikaze.thing-printer.com/apt/public.gpg | apt-key add -
echo "deb [arch=armhf] http://kamikaze.thing-printer.com/apt ./" >> /etc/apt/sources.list
apt-get update
apt-get install redeem
```

### Source install

```
apt-get install swig python-smbus
mkdir -p /usr/src
cd /usr/src
git clone https://github.com/intelligent-agent/redeem.git
cd redeem
make install
mkdir -p /etc/redeem
cp configs/* /etc/redeem
cp data/* /etc/redeem
```

### Source install with Python virtual environments

Using Python `virtualenv` is the suggested installation method when running from source for anything more than casual development.  Virtual environments allow multiple, independent installs of Redeem that are isolated from each other and other applications on the system.

The overview of the virtual structure includes directories in `/usr/local`, one for each working copy of Redeem that is desired.  The script for starting Redeem is modified to activate the selected virtual environment and start the service.

Note that the `2.1.x` and later branches of redeem need `pip` version 10.  This setup is done as `root`.

1. `cd /usr/local/lib/python2.7/dist-packages`

2. Delete the installed Redeem python packages from this directory, but keep the OctoPrint plugin.  `rm Redeem* redeem*`

3. `cd /usr/local`

4. Create the virtual environment with `virtualenv 2.2`  This will create a directory named `2.2` that will be the root of that virtual environment.  The name given name, `2.2`, is for demonstration purposes, feel free to choose a different name.

5. `cd 2.2`

6. Allow the use of system libraries with `rm lib/python/2.7/no-global-site-packages.txt`

7. Make the virtual environment active with `source bin/activate`.  This step isn't needed to edit files, but the virtual environment should be active when running `setup.py`.  In order to indicate that a virtual environment is active, the command prompt will have the environment name prefixed to the command prompt, like `(2.2) root@kamikaze:/usr/local/2.2`

8. Create a directory for the git repository, and clone it.

   ```
   mkdir src
   cd src
   git clone https://github.com/intelligent-agent/redeem.git
   cd redeem
   git checkout origin/2.2.x
   ```
   
9. Get things set up with `python setup.py develop`

10. `cd /usr/local/bin`

11. Create a file named `redeem-selection` with this script:

    ```
    #!/bin/sh
    echo "2.2"
    ```

    Make it executable with `chmod +x redeem-selection`
    This is the file that will be edited to change the selected Redeem virtual environment that is run as the redeem service.  It's name should match the virtual environment selected above.  Eventually, this file (which is a hack) will be replaced with a UI and proper interface.

12. Edit `redeem`, replacing it with:

    ```
    #!/bin/bash
    source /usr/local/`redeem-selection`/bin/activate
    echo "Starting Redeem from " $PATH
    /usr/local/`redeem-selection`/bin/redeem
    ```

13. Redeem can now be restarted, either via OctoPrint or `systemctl restart redeem`

When adding a new working copy, follow steps 3-9 with a different virtual environment directory name.  Edit `/usr/local/bin/redeem-selection` to select the desired directory. The other steps are only needed once for configuraion.

