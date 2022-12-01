"""Implementing a queue via a circular list."""

from __future__ import annotations
from typing import (
    Generic, TypeVar, Iterable,
)

T = TypeVar('T')


class Link(Generic[T]):
    """Doubly linked link."""

    val: T
    prev: Link[T]
    next: Link[T]

    def __init__(self, val: T, p: Link[T], n: Link[T]):
        """Create a new link and link up prev and next."""
        self.val = val
        self.prev = p
        self.next = n


def insert_after(link: Link[T], val: T) -> None:
    """Add a new link containing avl after link."""
    new_link = Link(val, link, link.next)
    new_link.prev.next = new_link
    new_link.next.prev = new_link

def inser_before(link: Link[T], val: T) -> None:
    """Add a new link containin val before link"""
    new_link = Link(val, link.prev, link)
    new_link.prev.next = new_link
    new_link.next.prev = new_link


def remove_link(link: Link[T]) -> None:
    """Remove link from the list."""
    link.prev.next = link.next
    link.next.prev = link.prev


class DLList(Generic[T]):
    """
    Wrapper around a doubly-linked list.

    This is a circular doubly-linked list where we have a
    dummy link that function as both the beginning and end
    of the list. By having it, we remove multiple special
    cases when we manipulate the list.

    >>> x = DLList([1, 2, 3, 4])
    >>> print(x)
    [1, 2, 3, 4]
    """

    head: Link[T]  # Dummy head link

    def __init__(self, seq: Iterable[T] = ()):
        """Create a new circular list from a sequence."""
        # Configure the head link.
        # We are violating the type invariants this one place,
        # but only here, so we ask the checker to just ignore it.
        # Once the head element is configured we promise not to do
        # it again.
        self.head = Link(None, None, None)  # type: ignore
        self.head.prev = self.head
        self.head.next = self.head

        # Add elements to the list, exploiting that self.head.prev
        # is the last element in the list, so appending means inserting
        # after that link.
        for val in seq:
            insert_after(self.head.prev, val)

    def __str__(self) -> str:
        """Get string with the elements going in the next direction."""
        elms: list[str] = []
        link = self.head.next
        while link and link is not self.head:
            elms.append(str(link.val))
            link = link.next
        return f"[{', '.join(elms)}]"
    __repr__ = __str__  # because why not?


class LinkedListdeque(Generic[T]):
    """A queue of type-T elements."""

    def __init__(self) -> None:
        """Make a new queue."""
        self.queue = DLList()

    def __str__(self) -> str:
        return str(self.queue)

    def __eq__(self, other: object) -> bool:
        return self.queue == other.queue

    def is_empty(self) -> bool:
        """Check if this queue is empty."""
        if self.queue.head.next == self.queue.head:
            return True
        else:
            return False

    def enqueue(self, x: T, last=True) -> None:
        """Add x to the end of this queue.
        If elements has to be added to the front, end=False"""
        if last:
            insert_after(self.queue.head.prev, x)
        else: 
            inser_before(self.queue.head.next, x)

    def front(self) -> T:
        """Get the front element of the queue."""
        return self.queue.head.next.val
    
    def end(self) -> T:
        """Get the last element of the queue"""
        return self.queue.head.prev.val

    def dequeue(self, front=True) -> T:
        """Get the front element, remove it from the queue, and return it. 
        If we want the last element dequeued front=False"""
        if front:
            elm = self.queue.head.next
            remove_link(elm)
        else: 
            elm = self.queue.head.prev
            remove_link(elm)
        return elm.val

class ListDeque(Generic[T]):
    """A queue of type-T elements."""

    def __init__(self) -> None:
        """Make a new queue."""
        self.queue = []

    def __str__(self) -> str:
        return "{}".format(self.queue)

    def __eq__(self, other: object) -> bool:
        return self.queue == other.queue

    def is_empty(self) -> bool:
        """Check if this queue is empty."""
        if len(self.queue)==0:
            return True
        else:
            return False

    def enqueue(self, x: T, last=True) -> None:
        """Add x to the end of this queue.
        If elements has to be added to the front, end=False"""
        if last:
            self.queue.append(x)
        else: 
            self.queue.insert(0,x)

    def front(self) -> T:
        """Get the front element of the queue."""
        return self.queue[0]
    
    def end(self) -> T:
        """Get the last element of the queue"""
        return self.queue[-1]

    def dequeue(self, front=True) -> T:
        """Get the front element, remove it from the queue, and return it. 
        If we want the last element dequeued front=False"""
        if front:
            elm = self.queue[0]
            self.queue.pop(0)
        else: 
            elm = self.queue[-1]
            self.queue.pop(-1)
        return elm

