obj-m += eudyptula_1.o
	KERNEL_VER ?= $(shell uname -r)
	KERNEL_PATH ?= /lib/modules/$(KERNEL_VER)/build

all:
	make -C $(KERNEL_PATH) M=$(PWD) modules

clean:
	make -C $(KERNEL_PATH) M=$(PWD) clean
