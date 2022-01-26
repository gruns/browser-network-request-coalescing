# test browser network request coalescing

- add two DNS records that point to `127.0.0.1` in your `/etc/hosts`
  file:

    ```
    127.0.0.1	    lh1
    127.0.0.1	    lh2
    ```

- host this directory. eg with
  [http-server](https://www.npmjs.com/package/http-server)

    ```
    http-server -p 9090
    ```

- start the tcp-aware HTTP server

    ```
    ./server.py
    ```

- open http://127.0.0.1:9090/two-images.html in your browser

- monitor the TCP connections in `server.py`'s output
