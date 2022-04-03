host:
    ports:
        http: 80
        https: 443

domain:
    name: example.com

services:
    my-service:
        context: my-service
        sslMode: CRT # [PEM,CRT]
        certs: ssl
        keys: ssl
        ou: organizational_unit
        requireBaseDNS: true

ca:
    context: ca
    name: ca
    c: US
    st: TX
    l: Austin
    o: organization
    ou: organizational_unit
    cn: common_name
