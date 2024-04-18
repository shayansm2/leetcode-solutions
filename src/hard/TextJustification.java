package hard;

import java.util.ArrayList;
import java.util.List;

public class TextJustification {
    public static void main(String[] args) {
        System.out.println(new TextJustification().fullJustify(
                new String[]{"This", "is", "an", "example", "of", "text", "justification."},
                16)
        );

        System.out.println(new TextJustification().fullJustify(
                new String[]{"What", "must", "be", "acknowledgment", "shall", "be"},
                16)
        );

        System.out.println(new TextJustification().fullJustify(
                new String[]{"Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"},
                20)
        );
    }

    public List<String> fullJustify(String[] words, int maxWidth) {
        int charCounter = 0;
        List<String> lineWords = new ArrayList<>();
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (word.length() + charCounter > maxWidth) {
                result.addLast(fullJustifyLine(lineWords, maxWidth));
                lineWords = new ArrayList<>();
                charCounter = 0;
            }

            charCounter += word.length() + 1;
            lineWords.addLast(word);
        }

        if (charCounter > 0) {
            result.addLast(leftJustifyLine(lineWords, maxWidth));
        }

        return result;
    }

    public String fullJustifyLine(List<String> words, int maxWidth) {
        if (words.size() == 1) {
            return leftJustifyLine(words, maxWidth);
        }

        int availableSpaces = maxWidth;
        for (String word : words) {
            availableSpaces -= word.length();
        }

        int spaceCount = availableSpaces / (words.size() - 1);
        int oneMoreSpaceCount = availableSpaces % (words.size() - 1);

        StringBuilder result = new StringBuilder(words.getFirst());
        for (int i = 1; i < words.size(); i++) {
            if (oneMoreSpaceCount > 0) {
                oneMoreSpaceCount--;
                result.append(" ".repeat(spaceCount + 1));
            } else {
                result.append(" ".repeat(spaceCount));
            }

            result.append(words.get(i));
        }
        return result.toString();
    }

    public String leftJustifyLine(List<String> words, int maxWidth) {
        String result = String.join(" ", words);
        result += " ".repeat(maxWidth - result.length());
        return result;
    }
}
