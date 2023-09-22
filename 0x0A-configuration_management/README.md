<h1 align='center'> Configuration Management</h1>

<p align='center'><image src='img/pplogo.svg.png' width=500></p>

Configuration Management entails handling changes to a system so that the
system remains robust

One of the most popular configuration management tools is *Puppet* and is
commonly used to manage nodes in servers. This repository will contain
simple manifests created using *Puppet*

## Key Info

* manifests are code files written to manage key nodes
* puppet has several resource types:
  * Cron
  * Exec
  * File
  * Group
  * Notify
  * Package
  * Service
  * User
* you can also write custom resources to suit your needs
* Multiple resources can be combined using classes

* Puppet uses a wide range of attribute names and values to define and manage resources in Puppet manifests. These attributes vary depending on the type of resource being managed (e.g., files, packages, services) and the specific resource provider. Here are some common attributes and values used in Puppet:

  **For All Resources:**
  
  1. `ensure`: This attribute is used to specify the desired state of a resource, such as 'present' or 'absent'. For example, `ensure => present` ensures that a resource exists, while `ensure => absent` ensures that it does not exist.
  
  2. `name` or `title`: This attribute typically represents the name or identifier of the resource.
  
  **File Resources:**
  
  1. `path`: The file path of the resource.
  
  2. `content`: The content that should be present in the file.
  
  3. `owner` and `group`: The owner and group of the file.
  
  4. `mode`: The file permissions (e.g., '0644').
  
  **Package Resources:**
  
  1. `name`: The name of the package to be managed.
  
  2. `ensure`: Specifies whether the package should be 'installed', 'latest', 'absent', etc.
  
  **Service Resources:**
  
  1. `name`: The name of the service to manage.
  
  2. `ensure`: Specifies whether the service should be 'running', 'stopped', or 'disabled'.
  
  3. `enable`: Determines whether the service should start at boot.
  
  **User and Group Resources:**
  
  1. `name`: The name of the user or group.
  
  2. `ensure`: Specifies whether the user or group should be 'present' or 'absent'.
  
  3. `uid` and `gid`: User and group IDs, respectively.
  
  **Exec Resources:**
  
  1. `command`: The command to execute.
  
  2. `unless` and `onlyif`: Conditions to determine whether the command should run.
  
  **Package Repository Resources (e.g., Yum or Apt):**
  
  1. `name`: The name of the repository.
  
  2. `baseurl`, `mirrorlist`, or `gpgkey`: Repository-specific attributes for configuration.
  
  **Class Declarations:**
  
  1. `include`: Includes a class.
  
  2. `require`: Specifies class dependencies.
  
  3. `params`: A common pattern for passing parameters to classes.
  
  These are just some examples of common attributes and values used in Puppet manifests. The specific attributes and values can vary depending on the resource type and the Puppet module or provider being used. Puppet's documentation and the documentation for specific modules/providers provide detailed information on available attributes and their usage.
  