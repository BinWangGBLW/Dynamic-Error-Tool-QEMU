#!/bin/bash

rm -rf output.txt
../x86_64-softmmu/qemu-system-x86_64 -enable-kvm -m 2048 -smp 1 -boot order=dc -hda /home/binqbu2002/qemu-xuniji/centos.img &
sleep 120
echo "Teminal QEMU process" 
kill -9 `ps -eo pid,cmd | grep qemu-system-x86_64 | grep -v grep | awk 'NR==1{print $1}'` 
