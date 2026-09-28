# Chapter 13: Adaptive replacement cache

## Overview

The Adaptive Replacement Cache (ARC) balances recency and frequency rather
than committing to only one replacement policy. It tracks four ordered lists:
`T1` and `T2` hold cached pages, while `B1` and `B2` keep identifiers of
recently evicted pages as ghost history. The target `p` adapts the size of the
recency side based on ghost hits. `T1` represents pages seen once recently;
`T2` represents pages used more than once recently.

In each list, the least-recently-used page is at the front and the most-recently
used page is at the end. Ghost lists contain identifiers only, not cached data.

## Pseudocode

```text
function ACCESS(x):
	if x is in T1 or T2:                       # real cache hit
		if x is in T1:
			remove x from T1
			insert x at MRU end of T2
		else:
			move x to MRU end of T2
		return HIT

	if x is in B1:                             # recency ghost hit
		delta = max(1, |B2| / |B1|)
		p = min(c, p + delta)
		REPLACE(x)
		remove x from B1
		fetch x from backing store
		insert x at MRU end of T2
		return GHOST_HIT_B1

	if x is in B2:                             # frequency ghost hit
		delta = max(1, |B1| / |B2|)
		p = max(0, p - delta)
		REPLACE(x)
		remove x from B2
		fetch x from backing store
		insert x at MRU end of T2
		return GHOST_HIT_B2

	L1 = |T1| + |B1|
	L2 = |T2| + |B2|
	if L1 == c:
		if |T1| < c:
			remove LRU entry of B1
			REPLACE(x)
		else:
			remove LRU entry of T1
	else if L1 < c and L1 + L2 >= c:
		if L1 + L2 == 2c:
			remove LRU entry of B2
		REPLACE(x)

	fetch x from backing store
	insert x at MRU end of T1
	return MISS

function REPLACE(x):
	if T1 is not empty and (|T1| > p or (x is in B2 and |T1| == p)):
		move LRU entry of T1 to MRU end of B1
	else:
		move LRU entry of T2 to MRU end of B2
```

## Python implementation

The complete implementation and the Chapter 13 cache trace are in
[code/adaptive_replacement_cache.py](../../code/adaptive_replacement_cache.py).
Its `access(page, fetch)` method returns the fetched or cached value along with
the result kind: `hit`, `ghost_hit_b1`, `ghost_hit_b2`, or `miss`.

Run the implementation directly to print the list state after each access in
the four-slot example. `p` moves up when a page in `B1` is requested again and
down when a page in `B2` is requested again, allowing ARC to adapt between
recency and frequency.

