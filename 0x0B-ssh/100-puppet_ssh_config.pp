file { '/home/ubuntu/.ssh/config':  # Replace with the correct path
    ensure  => present,  # Make sure the file exists.
    content => @(END)
User ubuntu
IdentityFile ~/.ssh/school
HostName 98.98.98.98
PasswordAuthentication no
ChallengeResponseAuthentication no
END
    owner   => 'ubuntu',  # Replace with the correct owner
    group   => 'ubuntu',  # Replace with the correct group
    mode    => '0600',    # Set appropriate permissions
}
