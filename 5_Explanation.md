# Problem 5

##    Time complexity

###       TrieNode 
            * O(1) insert
            * O(c * d) suffixes
                c - number of children per node
                d - depth of trie
###       Trie
            * O(n) insert
            * O(n) find



##    Space Complexity: 

###        TrieNode
            * O(1) insert
            * O(l * n) suffixes
                l - number of letters in word
                n - number of words in tree
###       Trie
            * O(n) insert
            * O(1) find