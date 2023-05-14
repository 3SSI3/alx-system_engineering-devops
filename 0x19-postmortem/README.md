# POSTMORTERM :clipboard:.
**Duration: 30 mins** (13:20pm ~ 13:30pm EAT).

Upon assisting our client who was in another country, we need access to connect to her server. However, while trying to connect to the clients server via SSH, we were not granted permission to access our client's server.

**Impact**: Due to the inability to access our client's server on time, we experienced disruptions that impacted both the client and our scheduled meetings with other clients.

**Root cause**: Incorrect unauthorized ssh keys.

**TIMELINE**;
* 13:20PM :- Issue was detected when monitoring system triggered the  "permission denied" error when connecting to the client's server.
* 13:22PM :- Several other users reported similar issues.
* 13:23PM :- The initial investigation paths taken with the assumption that the issue was related to the local SSH key configuration files.
* 13:40PM :- The server administrator was alerted to the issue and began investigating.
* 13:44PM:- However the server administrator identified that actually the private key file used for authentication had incorrect permissions.
* 13:45PM :- The server administrator corrected the permissions on the private key file.
* 13:50PM :- Incident closed and was able to connect to the server via SSH successfully.

### Root cause and Resolution;
* The issue was caused by a misconfiguration of the SSH server, that resulted in incorrect permissions on the private key file user used for authentication.
 A configuration file was inadvertently changed, which resulted in the incorrect permissions on the private key life.

* The issue was fixed by updating the SSH configuration file to allow the customer's user account access. This was done by updating the file permission like adding the SSH key to the authorized_keys file on the server to ensure that the engineer had read and write access to the file.

### Corrective and preventative measures;
In order to avoid such issues occurring in the future we had to; 
* Ensure proper user permissions are set for all users accessing the server through SSH.
* Regular review and update of the server's access controls and configurations.
* Also setting up additional monitoring and alerts to detect quickly and resolve similar issues in the future.
* Finally, by training and educating server administrators/ engineers on best practices for configuring and maintaining SSH access.
