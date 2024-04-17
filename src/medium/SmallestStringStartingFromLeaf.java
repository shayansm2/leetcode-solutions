package medium;

import lib.TreeNode;

import java.util.ArrayList;
import java.util.Arrays;

public class SmallestStringStartingFromLeaf {
    public static void main(String[] args) {
        TreeNode tree = new TreeNode(0,
                new TreeNode(1,
                        new TreeNode(3),
                        new TreeNode(4)
                ),
                new TreeNode(2,
                        new TreeNode(3),
                        new TreeNode(4)
                )
        );
        System.out.println(new SmallestStringStartingFromLeaf().smallestFromLeaf(tree));
        tree = new TreeNode(25,
                new TreeNode(1,
                        new TreeNode(1),
                        new TreeNode(3)
                ),
                new TreeNode(3,
                        new TreeNode(0),
                        new TreeNode(2)
                )
        );
        System.out.println(new SmallestStringStartingFromLeaf().smallestFromLeaf(tree));
        tree = new TreeNode(2,
                new TreeNode(2, null, new TreeNode(1, new TreeNode(0), null)),
                new TreeNode(1, new TreeNode(0), null)
        );
        System.out.println(new SmallestStringStartingFromLeaf().smallestFromLeaf(tree));
    }

    public String smallestFromLeaf(TreeNode root) {
        ArrayList<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        ArrayList<int[]> parentsValues = new ArrayList<>();
        parentsValues.add(new int[]{});
        int[] minValue = new int[]{};

        while (!queue.isEmpty()) {
            TreeNode node = queue.removeFirst();
            int[] parentsValue = parentsValues.removeFirst();
            int[] nodeValue = Arrays.copyOf(parentsValue, parentsValue.length + 1);
            nodeValue[parentsValue.length] = node.val;

            if (node.left != null) {
                queue.addFirst(node.left);
                parentsValues.addFirst(nodeValue);
            }

            if (node.right != null) {
                queue.addFirst(node.right);
                parentsValues.addFirst(nodeValue);
            }

            if (node.left == null && node.right == null) {
                minValue = getLexicographicMin(minValue, nodeValue);
            }
        }

        return represent(minValue);
    }

    private static void printArray(int[] a) {
        for (int i = 0; i < a.length; i++) {
            System.out.print(i);
        }
        System.out.println();
    }

    public static int[] getLexicographicMin(int[] a, int[] b) {
        if (a.length == 0) {
            return b;
        }

        if (b.length == 0) {
            return a;
        }

        for (int i = 0; i < Math.min(a.length, b.length); i++) {
            int indexA = a.length - i - 1;
            int indexB = b.length - i - 1;
            if (a[indexA] > b[indexB]) {
                return b;
            } else if (a[indexA] < b[indexB]) {
                return a;
            }
        }

        if (a.length < b.length) {
            return a;
        }

        return b;
    }

    public static String represent(int[] a) {
        StringBuilder result = new StringBuilder();
        for (int i = a.length - 1; i >= 0; i--) {
            result.append((char) (a[i] + 97));
        }
        return result.toString();
    }
}
