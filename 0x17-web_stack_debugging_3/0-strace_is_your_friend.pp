# Fixx why Aphache is returning a 500 error then automte using puppet.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin','/usr/bin']
}
