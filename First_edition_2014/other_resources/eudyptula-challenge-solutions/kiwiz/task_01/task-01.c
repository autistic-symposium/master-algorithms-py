#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

static int __init setup(void) {
    printk(KERN_DEBUG "Hello World!");

    return 0;
}

static void __exit teardown(void) {
}

module_init(setup);
module_exit(teardown);
