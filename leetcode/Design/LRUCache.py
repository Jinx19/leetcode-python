from leetcode.LinkedList.ListNode import ListNode


class LRUCache:
    def repalce(self,key:'int'):
        pre = self.head
        curr = pre.next
        while curr is not None:
            if curr.val == key:
                if curr.next is None:
                    return
                pre.next = curr.next
                break
            pre= pre.next
            curr = curr.next

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = ListNode(key)

    def appendtail(self,key:'int',value:'int'):
        self.hashmap[key] = value
        dummpy = self.head
        while dummpy.next is not None:
            dummpy = dummpy.next
        dummpy.next = ListNode(key)

    def deleteused(self):
        dummpy = self.head
        if dummpy.next is not None:
            self.hashmap.pop(dummpy.next.val)
            dummpy.next = dummpy.next.next


    def __init__(self, capacity: 'int'):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode(-1)

    def get(self, key: 'int') -> 'int':
        if key in self.hashmap:
            self.repalce(key)
            return self.hashmap[key]
        else:
            return -1

    def put(self, key: 'int', value: 'int') -> 'None':
        if len(self.hashmap) == self.capacity and key not in self.hashmap:
            self.deleteused()
        if key not in self.hashmap:
            self.appendtail(key,value)
        else:
            self.hashmap[key] = value
            self.repalce(key)
#
# cache = LRUCache(2)
# print(cache.put(1,1))
# print(cache.put(2,2))
# print(cache.get(1))
# print(cache.put(3,3))
# print(cache.get(2))
# print(cache.put(4,4))
# print(cache.get(1))
# print(cache.get(3))
# print(cache.get(4))
#
cache = LRUCache(2)
print(cache.get(2))
print(cache.put(2,6))
print(cache.get(1))
print(cache.put(1,5))
print(cache.put(1,2))
print(cache.get(1))
print(cache.get(2))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)