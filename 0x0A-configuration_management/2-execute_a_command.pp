# Execute a command kills a process
exec { 'pkill killmenow':
	path => '/usr/bin:/usr/sbin:/bin'
}

