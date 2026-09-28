"""Adaptive Replacement Cache (ARC).

Implements the four-list ARC policy described in Chapter 13. T1 and T2 hold
cached values; B1 and B2 retain ghost identifiers for evicted entries.

Based on Megiddo and Modha, "ARC: A Self-Tuning, Low Overhead Replacement
Cache," FAST '03, USENIX, 2003.
"""

from collections import OrderedDict


class ARC:
    """Adaptive replacement cache balancing recency and frequency."""

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")

        self.c = capacity
        self.p = 0
        self.T1 = OrderedDict()  # Recent pages seen once
        self.T2 = OrderedDict()  # Frequently/recently reused pages
        self.B1 = OrderedDict()  # Ghost history for T1
        self.B2 = OrderedDict()  # Ghost history for T2

    def _replace(self, page):
        """Evict one resident page and record its identifier as a ghost."""
        evict_from_t1 = len(self.T1) > self.p or (
            page in self.B2 and len(self.T1) == self.p
        )
        if self.T1 and evict_from_t1:
            evicted, _ = self.T1.popitem(last=False)
            self.B1[evicted] = None
        else:
            evicted, _ = self.T2.popitem(last=False)
            self.B2[evicted] = None

    def access(self, page, fetch):
        """Access ``page``, fetching its value on a miss or ghost hit.

        Args:
            page: Hashable page identifier.
            fetch: Callable that returns the page's value given its identifier.

        Returns:
            A pair ``(value, kind)``, where kind is ``hit``, ``ghost_hit_b1``,
            ``ghost_hit_b2``, or ``miss``.
        """
        if page in self.T1:
            value = self.T1.pop(page)
            self.T2[page] = value
            return value, "hit"

        if page in self.T2:
            self.T2.move_to_end(page)
            return self.T2[page], "hit"

        if page in self.B1:
            delta = max(1, len(self.B2) // len(self.B1))
            self.p = min(self.c, self.p + delta)
            self._replace(page)
            del self.B1[page]
            value = fetch(page)
            self.T2[page] = value
            return value, "ghost_hit_b1"

        if page in self.B2:
            delta = max(1, len(self.B1) // len(self.B2))
            self.p = max(0, self.p - delta)
            self._replace(page)
            del self.B2[page]
            value = fetch(page)
            self.T2[page] = value
            return value, "ghost_hit_b2"

        l1 = len(self.T1) + len(self.B1)
        l2 = len(self.T2) + len(self.B2)
        if l1 == self.c:
            if len(self.T1) < self.c:
                self.B1.popitem(last=False)
                self._replace(page)
            else:
                self.T1.popitem(last=False)
        elif l1 < self.c and l1 + l2 >= self.c:
            if l1 + l2 == 2 * self.c:
                self.B2.popitem(last=False)
            self._replace(page)

        value = fetch(page)
        self.T1[page] = value
        return value, "miss"

    def state(self):
        """Return a snapshot of the list contents and adaptive target ``p``."""
        return {
            "T1": list(self.T1),
            "T2": list(self.T2),
            "B1": list(self.B1),
            "B2": list(self.B2),
            "p": self.p,
        }


if __name__ == "__main__":
    # Four-slot cache trace from Chapter 13, section 13.1.3.
    cache = ARC(capacity=4)
    sequence = ["A", "B", "C", "D", "A", "E", "B", "F", "D", "A"]

    for page in sequence:
        _, kind = cache.access(page, fetch=lambda key: key)
        current = cache.state()
        print(
            f"{page:2s} {kind:12s} T1={current['T1']} T2={current['T2']} "
            f"B1={current['B1']} B2={current['B2']} p={current['p']}"
        )
