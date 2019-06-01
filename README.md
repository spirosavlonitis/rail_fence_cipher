# rail_fence_cipher
Encode and decode a string using the Rail Fence Cipher.

A simple shell example:

```shell
>>> from rail_fence_cipher import RailFenceCipher
>>> obj = RailFenceCipher()
>>> obj.encode_rail_fence_cipher('foo bar buzz', 7)
'fozoz ubba r'
>>> obj.decode_rail_fence_cipher('fozoz ubba r', 7)
'foo bar buzz'
```
