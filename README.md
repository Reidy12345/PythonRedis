# PythonRedis

In an effort to understand Redis a little under the hood, we create a mini version of Redis, using Python, that supports the following commands

- GET \<key>
- SET \<key> \<value>
- DELETE \<key>
- FLUSH

And will support the following data types

- Strings (supported)
- String Arrays (currently unsupported)

For extra reading, and to add more features, see https://charlesleifer.com/blog/building-a-simple-redis-server-with-python/ and https://redis.io/docs/latest/develop/reference/protocol-spec/
