#
# Regular cron jobs for the robotkernel-service-helper package
#
0 4	* * *	root	[ -x /usr/bin/robotkernel-service-helper_maintenance ] && /usr/bin/robotkernel-service-helper_maintenance
