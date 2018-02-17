# System auto installer By MR.bar
# Script by Ubaii ID
import os, time

def auto():
# delete bash lama.
	os.system('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
# Ganti bash baru.
	time.sleep(2)
	baru = """command_not_found_handle() {
	/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

clear"""


	f = open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w')
	f.write(baru)
	f.close
# profile.sh auto tiban
	niban = """for i in /data/data/com.termux/files/usr/etc/profile.d/*.sh; do
	if [ -r $i ]; then
		. $i
	fi
done
unset i

# Source etc/bash.bashrc and ~/.bashrc also for interactive bash login shells:
if [ "$BASH" ]; then
        if [[ "$-" == *"i"* ]]; then
                if [ -r /data/data/com.termux/files/usr/etc/bash.bashrc ]; then
                        . /data/data/com.termux/files/usr/etc/bash.bashrc
                fi
                if [ -r /data/data/com.termux/files/home/.bashrc ]; then
                        . /data/data/com.termux/files/home/.bashrc
                fi
        fi
fi

python2 lock.py -l"""
	f = open('/data/data/com.termux/files/usr/etc/bash.basrc', 'w')
	f.write(niban)
	f.close
	os.system('clear')
	print('DONE.')
	exit()
# Done. :)

##############################
# fb : @ubaiiid.rebornii
# ig : @ubaii.id
# yt : youtube.com/Ubaii_ID
##############################
auto()
