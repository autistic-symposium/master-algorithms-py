This is Task 02 of the Eudyptula Challenge
------------------------------------------

Now that you have written your first kernel module, it's time to take
off the training wheels and move on to building a custom kernel.  No
more distro kernels for you.  For this task you must run your own
kernel.  And use git!  Exciting, isn't it?  No?  Oh, ok...

The tasks for this round are:
  - Download Linus's latest git tree from git.kernel.org (you have to
    figure out which one is his.  It's not that hard, just remember what
    his last name is and you should be fine.)
  - Build it, install it, and boot it.  You can use whatever kernel
    configuration options you wish to use, but you must enable
    CONFIG_LOCALVERSION_AUTO=y.
  - Show proof of booting this kernel.  Bonus points if you do it on a
    "real" machine, and not a virtual machine (virtual machines are
    acceptable, but come on, real kernel developers don't mess around
    with virtual machines, they are too slow.  Oh yeah, we aren't real
    kernel developers just yet.  Well, I'm not anyway, I'm just a
    script...)  Again, proof of running this kernel is up to you, I'm
    sure you can do well.

Hint, you should look into the 'make localmodconfig' option, and base
your kernel configuration on a working distro kernel configuration.
Don't sit there and answer all 1625 different kernel configuration
options by hand, even I, a foolish script, know better than to do that!

After doing this, don't throw away that kernel, git tree, and
configuration file.  You'll be using it for later tasks.  A working
kernel configuration file is a precious thing, all kernel developers
have one they have grown and tended to over the years.  This is the
start of a long journey with yours.  Don't discard it like was a broken
umbrella, it deserves better than that.
