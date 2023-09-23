# SSH

SSH is a secure protocol used as the primary means of connecting to Linux servers remotely. It provides a text-based interface by spawning a remote shell. 

## Directory Files

* [0-use_a_private_key ](0-use_a_private_key ) - access remote server via ssh
* [1-create_ssh_key_pair ](1-create_ssh_key_pair ) - a Bash script that creates an RSA key pair.
  * Name of the created private key must be school
  * Number of bits in the created key to be created 4096
  * The created key must be protected by the passphrase betty
* [2-ssh_config](2-ssh_config) - create a config file for ssh
* [100-puppet_ssh_config.pp](100-puppet_ssh_config.pp) - create a puppet manifest to generate a config file for ssh
