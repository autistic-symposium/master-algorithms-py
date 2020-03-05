/*
 * Eudyptula #1
 */

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

int init_module(void)
{
	printk(KERN_DEBUG "Ola Mundo!\n");
	return 0;
}

void cleanup_module(void)
{
	printk(KERN_DEBUG "Unloading exer 1! Goodbye!!!\n");
}


MODULE_LICENSE("GLP");
MODULE_AUTHOR("7e1cf379bd3d");
