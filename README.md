# http-header-reflector
Simple Python HTTP Server which reflects the client http request header in server logs to see the header fields forwarded by Kubernetes Load Balances and Ingress Controllers. This comes in handy for various validations to see the request received from Envoy/Linkerd Proxy as well.

Container Image - https://hub.docker.com/r/subodhp/http-echo/

Command Backup 

1. Remove the taint on master node 

kubectl taint nodes --all node-role.kubernetes.io/master-
