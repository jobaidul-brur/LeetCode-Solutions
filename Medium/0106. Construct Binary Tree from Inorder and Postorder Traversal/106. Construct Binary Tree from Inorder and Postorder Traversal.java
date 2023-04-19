/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    Map<Integer, Integer> pos = new HashMap<>();

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        for (int i = 0; i < inorder.length; i++) {
            pos.put(inorder[i], i);
        }
        return buildTree(inorder, 0, inorder.length-1, postorder, 0, postorder.length-1);
    }
    public TreeNode buildTree(int[] inorder, int startIn, int endIn, int[] postorder, int startPost, int endPost) {
        if (startIn > endIn || startPost > endPost) return null;

        TreeNode root = new TreeNode(postorder[endPost]);
        int midIndex = pos.get(postorder[endPost]);
        root.left = buildTree(inorder, startIn, midIndex-1, postorder, startPost, startPost+midIndex-startIn-1);
        root.right = buildTree(inorder, midIndex+1, endIn, postorder, startPost+midIndex-startIn, endPost-1);

        return root;
    }
}