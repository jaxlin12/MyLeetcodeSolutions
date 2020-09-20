#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def one_diff(self, s, t):
        count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1
            if count == 2:
                return False
        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(wordList) < 0:
            if endWord not in wordList:
                return 0
            if beginWord not in wordList:
                wordList.append(beginWord)
            dictionary = []
            for _ in range(len(wordList)):
                dictionary.append([])
            begin = None
            target = None

            for i in range(len(wordList)):
                if wordList[i] == beginWord:
                    begin = i
                if wordList[i] == endWord:
                    target = i

                for j in range(i+1, len(wordList)):
                    if j in dictionary[i]:
                        continue
                    if self.one_diff(wordList[i], wordList[j]):
                        dictionary[i].append(j)
                        dictionary[j].append(i)

            visted = [False] * len(wordList)
            
            length = 1
            queue = collections.deque()
            queue.append(begin)
            level_flag = begin
            while len(queue) != 0:
                i = queue.popleft()
                for index in dictionary[i]:
                    if not visted[index]:
                        visted[index] = True
                        if index == target:
                            return length + 1
                        queue.append(index)
                if i == level_flag and len(queue) != 0:
                    level_flag = queue[-1]
                    length += 1
            return 0
        else:
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: int
            """

            if endWord not in wordList or not endWord or not beginWord or not wordList:
                return 0

            # Since all words are of same length.
            L = len(beginWord)

            # Dictionary to hold combination of words that can be formed,
            # from any given word. By changing one letter at a time.
            all_combo_dict = defaultdict(list)
            for word in wordList:
                for i in range(L):
                    # Key is the generic word
                    # Value is a list of words which have the same intermediate generic word.
                    all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


            # Queue for BFS
            queue = collections.deque([(beginWord, 1)])
            # Visited to make sure we don't repeat processing same word.
            visited = {beginWord: True}
            while queue:
                current_word, level = queue.popleft()      
                for i in range(L):
                    # Intermediate words for current word
                    intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                    # Next states are all the words which share the same intermediate state.
                    for word in all_combo_dict[intermediate_word]:
                        # If at any point if we find what we are looking for
                        # i.e. the end word - we can return with the answer.
                        if word == endWord:
                            return level + 1
                        # Otherwise, add it to the BFS Queue. Also mark it visited
                        if word not in visited:
                            visited[word] = True
                            queue.append((word, level + 1))
                    all_combo_dict[intermediate_word] = []
            return 0




# @lc code=end

