# dirtravel
Crawls directory listing pages for directories

## Prevention

For nginx, set `autoindex` to off:

```
autoindex off;
```

For Apache and compatible servers:

Create a `.htaccess` file in the root directory of the website with the following line:

```
Options -Indexes
```
