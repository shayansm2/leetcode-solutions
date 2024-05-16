package medium;

import lib.TreeNode;

import java.util.ArrayList;

public class MaximumWidthBinaryTree {
    public static void main(String[] args) {
        System.out.println(
                new MaximumWidthBinaryTree().widthOfBinaryTree(
                        new TreeNode(1, new TreeNode(3, new TreeNode(5), null), new TreeNode(2))
                )
        );
    }

    public int widthOfBinaryTree(TreeNode root) {
        if (root.left == null && root.right == null) {
            return 1;
        }

        if (root.right == null) {
            return widthOfBinaryTree(root.left);
        }

        if (root.left == null) {
            return widthOfBinaryTree(root.right);
        }

        ArrayList<TreeNode> queue = new ArrayList<>();
        queue.addFirst(root);

        ArrayList<Integer> positions = new ArrayList<>();
        positions.addFirst(0);

        ArrayList<Integer> heights = new ArrayList<>();
        heights.addFirst(0);

        int maxWidth = 1, currentHeight = 0, offset = 0, minPosition = 0;
        while (!queue.isEmpty()) {
            TreeNode node = queue.removeLast();
            int position = positions.removeLast();
            int height = heights.removeLast();

            if (height > currentHeight) {
                currentHeight = height;
                minPosition = position;
                if (node.left != null) {
                    offset = 2 * position;
                } else if (node.right != null) {
                    offset = 2 * position + 1;
                }
            }

            if (node.left != null) {
                queue.addFirst(node.left);
                positions.addFirst(2 * position - offset);
                heights.addFirst(height + 1);
            }

            if (node.right != null) {
                queue.addFirst(node.right);
                positions.addFirst(2 * position + 1 - offset);
                heights.addFirst(height + 1);
            }

            maxWidth = Math.max(maxWidth, position - minPosition);
        }

        return maxWidth;
    }
}
