package medium;

import lib.TreeNode;

import java.util.ArrayList;

public class AddOneRowTree {
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            return new TreeNode(val, root, null);
        }

        ArrayList<TreeNode> queue = new ArrayList<>();
        ArrayList<Integer> depths = new ArrayList<>();
        queue.add(root);
        depths.add(1);
        while (!queue.isEmpty()) {
            TreeNode node = queue.removeFirst();
            Integer nodeDepth = depths.removeFirst();
            if (nodeDepth >= depth) {
                continue;
            }

            if (nodeDepth == depth - 1) {
                node.left = new TreeNode(val, node.left, null);
                node.right = new TreeNode(val, null, node.right);
                continue;
            }

            if (node.left != null) {
                queue.add(node.left);
                depths.add(nodeDepth + 1);
            }
            if (node.right != null) {
                queue.add(node.right);
                depths.add(nodeDepth + 1);
            }

        }
        return root;
    }
}