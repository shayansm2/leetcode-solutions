package medium;

import lib.TreeNode;

public class DeleteLeavesWithGivenValue {
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        if (shouldBeDeleted(root, target)) {
            return null;
        }

        root.left = removeLeafNodes(root.left, target);
        root.right = removeLeafNodes(root.right, target);
        return root;
    }

    private boolean shouldBeDeleted(TreeNode root, int target) {
        if (root == null) {
            return true;
        }

        if (root.val != target) {
            return false;
        }

        if (root.left == null && root.right == null) {
            return true;
        }

        return shouldBeDeleted(root.left, target) && shouldBeDeleted(root.right, target);
    }
}
