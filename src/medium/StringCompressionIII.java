package medium;

public class StringCompressionIII {
    public static void main(String[] args) {
        System.out.println(
                new StringCompressionIII().compressedString("edcba")
        );
        System.out.println(
                new StringCompressionIII().compressedString("abcde")
        );
        System.out.println(
                new StringCompressionIII().compressedString("aaaaaaaaaaaaaabb")
        );
        System.out.println(
                new StringCompressionIII().compressedString("aaaaaaaaay")
        );
    }

    public String compressedString(String word) {
        StringBuilder result = new StringBuilder();
        Character current = null;
        int count = 0;
        for (char ch : word.toCharArray()) {
            if (current == null) {
                current = ch;
                count = 1;
                continue;
            }
            if (ch == current) {
                count++;
                continue;
            }
            if (count >= 9) {
                result.repeat("9" + current, count / 9);
            }

            if (count % 9 > 0) {
                result.append(count % 9).append(current);
            }


            count = 1;
            current = ch;
        }
        if (count > 9) {
            result.repeat("9" + current, count / 9);
        }

        if (count % 9 > 0) {
            result.append(count % 9).append(current);
        }
        return result.toString();
    }
}
