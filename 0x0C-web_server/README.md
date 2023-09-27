# Web Servers

A Web Server's role is to provide static content to a client (e.g. a browser). In this directory I set up on NGINX web server host on `54.237.31.51` with the DNS of [comascript.tech](https://comascript.tech)

## Directory Files

* [0-transfer_file](0-transfer_file) - a Bash script that transfers a file from our client to a server
* [1-install_nginx_web_server](1-install_nginx_web_server) -a script that installs and configures the nginx server on ubuntu
* [2-setup_a_domain_name](2-setup_a_domain_name) - contains a domain name setup for an ip in which the server is running on
* [3-redirection](3-redirection) - a script that configures nginx to redirect traffic to another link when the /redirect_me directory is accessed
* [4-not_found_page_404](4-not_found_page_404) - configures a custom error 404 page when user enters an incorrect url directory
