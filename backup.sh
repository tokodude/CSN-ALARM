#!/bin/bash
# source: http://broexperts.com/how-to-backup-files-and-directories-in-linux-using-tar-cron-jobs/
#START
TIME=`date +%b-%d-%y`
FILENAME=backup-$TIME.tar.gz
SRCDIR=/home/pi		# Source directory
DESDIR=/home/pi/backup	# Destination of backup file.
tar -cpzf $DESDIR/$FILENAME $SRCDIR
#END
