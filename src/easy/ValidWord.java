public class ValidWord {
    public boolean isValid(String word) {
        if (word.length() < 3) {
            return false;
        }

        for (String i : new String[]{"@", "#", "$"}) {
            if (word.contains(i)) {
                return false;
            }
        }

        boolean hasVowel = false;
        for (char i : new char[]{'a', 'e', 'i', 'o', 'u'}) {
            if (word.contains(String.valueOf(i))) {
                hasVowel = true;
                break;
            }

            if (word.contains(String.valueOf(Character.toUpperCase(i)))) {
                hasVowel = true;
                break;
            }
        }
        if (!hasVowel) {
            return false;
        }

        boolean hasConsonant = false;
        String constantLetters = "BCDFGJKLMNPQSTVXZHRWY";
        for (char i : constantLetters.toCharArray()) {
            if (word.contains(String.valueOf(i))) {
                hasConsonant = true;
                break;
            }

            if (word.contains(String.valueOf(Character.toLowerCase(i)))) {
                hasConsonant = true;
                break;
            }
        }
        if (!hasConsonant) {
            return false;
        }
        return true;
    }
}
