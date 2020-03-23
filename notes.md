# Notes

Need a "new" script -- creates a new object and opens in editor
Need a "query" script or query view -- this gets the reference needed for specific object
Need like some sort of tag querying and tag management


Every object needs an associated json meta file, or there needs to be a singular
index file?



## Syntax

Going to have to have a special syntax to handle kofi specific things. Use yaml
at top?

When you first create something it goes in the cache


the three equals indicate the end of the object:

=== 
[[[uuid]]] -- link to specific object
{{{uuid}}} -- embed specific object
{{{query=somequery}}} --- embed results of a query
=== 

---
[meta information]
---

surrounding by 
{
}
means to create a new object (and replace with embedding)
