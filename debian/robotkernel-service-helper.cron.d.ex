#
# Regular cron jobs for the robotkernel-generator package
#
0 4	* * *	root	[ -x /usr/bin/robotkernel-generator_maintenance ] && /usr/bin/robotkernel-generator_maintenance
