# PythonRedis

In an effort to understand Redis a little under the hood, we create a mini version of Redis, using Python, that supports the following commands

- GET \<key>
- SET \<key> \<value>
- DELETE \<key>
- FLUSH
- MGET \<key 1> ... \<key n>
- MSET \<key 1> \<valu 1> ... \<key n> \<value n>

And will support the following data types

- Strings and Binary Data
- Numbers
- NULL
- Arrays (which may be nested)
- Dictionaries (which may be nested)
- Error messages

This repo follows the instruction of this tutorial https://charlesleifer.com/blog/building-a-simple-redis-server-with-python/
