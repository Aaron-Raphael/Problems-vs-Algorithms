# Problem 5

##    Time complexity

###       RouteTrieNode 
            * O(1) insert
###       RouteTrie
            * O(n) insert
            * O(l * d) find
                l - length if path
                d - depth of route
###       Router
            * O(n) add
            * O(n) split_path



##    Space Complexity: 

###        RouteTrieNode
            * O(n) insert
###       RouteTrie
            * O(n) insert
            * O(1) find
###       Router
            * O(n) add
            * O(n) split_path