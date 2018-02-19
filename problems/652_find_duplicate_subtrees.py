'''
URL: https://leetcode.com/problems/find-duplicate-subtrees/description/
Time complexity: O(n)
Space complexity: O(n^2)
'''

class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        serials = {}
        dups = []
        self.find_dups(serials, dups, root)
        print(serials)
        return dups

    def find_dups(self, serials, dups, curr_node):
        if curr_node is None:
            return "#" # Replacing null leaf nodes with '#' to differentiate between structures that have the exact same values where all nodes have the same value.

        '''
        Can't use inorder traversal because some trees that are mirrored across the root node will certainly produce a
        reversed serialized string but this reversed serialized string can be the same as the original string (i.e serialized string
        in original or mirroed tree is SYMMETRICAL). Not referring to symmetrical trees (we need asymmetrical trees that can
        produce symmetrical serialized strings to show that inorder cannot be used here - think of using only 0s and #s in some asymetrical tree).
        '''
        serial = self.find_dups(serials, dups, curr_node.right) + "," + str(curr_node.val) + "," + self.find_dups(serials, dups, curr_node.left)

        if serial in serials:
            if serials[serial] == 1:
                dups.append(curr_node)
            serials[serial] += 1
        else:
            serials[serial] = 1
        return serial
