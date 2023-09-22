# ensures mysql service is stopped
service {'mysql':
    ensure => 'stopped',
}
