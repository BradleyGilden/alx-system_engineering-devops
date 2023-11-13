# Takes care of Too many open files error by increasing traffic.

# Increase the ULIMIT of the default configuration
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Reload configurations
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
