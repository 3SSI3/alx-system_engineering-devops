# The script that increases the amount of traffic an Nginx can handle.
# Also increase ULIMIT of the default file.

exec { 'fix--for--nginx':
    command => 'sed -i "s/15/4096" /etc/default/nginx
    path    => '/usr/local/bin/:/bin/'
}


-> exec { 'nginx-restart':
   command => 'nginx restart',
   path    => '/etc/init.d/'
}