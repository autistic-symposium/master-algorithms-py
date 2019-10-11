1. Clone Linus’ repo and read Installing the kernel source:
```
$ git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
```

2. Generate .config and add CONFIG_LOCALVERSION_AUTO=y
```
$ make localmodconfig
```

3. Get an openssl header error, install lots of dev libraries
```
$ sudo apt-get install python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
```

4. Make! (It takes ~ 30 min)
```
$ make
```

5. Make module, install, add to grub 
```
$ make modules
$ sudo make modules_install 
$ sudo make install 
$ update-grub
```

6. Reboot machine. For ubuntu: press shift to get grub menu 

Profit!

Some tips:
* List of kernel addresses sorted in ascending order, from which it is simple to find the function that contains the offending address: 
```
$ nm vmlinux | sort | less 
```

Send
```
make && make modules && make modules_install && make install
```
