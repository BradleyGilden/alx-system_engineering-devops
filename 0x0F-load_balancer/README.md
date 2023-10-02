# Load Balancer

This directory contains scripts for setting up multiple NGINX servers with an HAProxy load balancer

# Directory Files

* [0-custom_http_response_header](0-custom_http_response_header) - adds custom header X-Served-By: $HOSTNAME for nginx server
* [1-install_load_balancer](1-install_load_balancer) - installs and Configures HAproxy on ubuntu machine
