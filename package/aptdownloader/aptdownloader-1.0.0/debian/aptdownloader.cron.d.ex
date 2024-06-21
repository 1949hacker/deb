#
# Regular cron jobs for the aptdownloader package.
#
0 4	* * *	root	[ -x /usr/bin/aptdownloader_maintenance ] && /usr/bin/aptdownloader_maintenance
