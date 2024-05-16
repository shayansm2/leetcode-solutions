import lib.TreeNode;

public class EvaluateBooleanBinaryTree {
    public boolean evaluateTree(TreeNode root) {
        if (root.val < 2) {
            return root.val == 1;
        }

        if (root.val == 3) {
            return evaluateTree(root.left) && evaluateTree(root.right);
        }

        if (evaluateTree(root.left)) {
            return true;
        }

        return evaluateTree(root.right);
    }
}
