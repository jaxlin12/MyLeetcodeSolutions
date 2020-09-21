#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            return
        self.content = {}
        self.capacity = capacity
        self.size = 0
        self.max_priority = None
        self.less_priority = None

    def get(self, key: int) -> int:
        if key in self.content and self.content[key] != None:
            node = self.content[key]
            self.update(key, node.val)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.content or self.content[key] == None:
            if self.size == 0:
                new_node = Node(key, value, None, None)
                self.content[key] = new_node
                self.less_priority = self.max_priority = new_node
                self.size += 1
            elif self.size < self.capacity:
                new_node = Node(key, value, None, None)
                self.content[key] = new_node
                new_node.prev = self.max_priority
                self.max_priority.next = new_node
                self.max_priority = new_node
                self.size += 1
            else:
                evit_node = self.less_priority
                self.content[evit_node.key] = None
                self.content[key] = evit_node
                evit_node.key = key
                if self.capacity != 1:
                    self.less_priority = self.less_priority.next
                self.less_priority.prev = None
                evit_node.val = value
                evit_node.next = None
                evit_node.prev = self.max_priority
                if self.capacity != 1:
                    self.max_priority.next = evit_node
                self.max_priority = evit_node
        else:
            self.update(key, value)


    def update(self, key, value):
        node = self.content[key]
        node.val = value
        if node == self.less_priority:
            if self.capacity != 1:
                self.max_priority.next = node
                node.prev = self.max_priority
                self.max_priority = node
                self.less_priority = node.next
                node.next.prev = node
                node.next = node
        elif node != self.max_priority:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.max_priority.next = node
            node.prev = self.max_priority
            node.next = None
            self.max_priority = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

