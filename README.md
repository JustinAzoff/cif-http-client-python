CIF HTTP Client
===============

Example
-------

    import cif_http_client

    http_options = {"verify": False} #don't verify ssl certs
    c = cif_http_client.Client("https://cif.example.net/api", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", http_options, nolog=True)
    records = c.search(q="example.com")
    for r in records:
        print r
