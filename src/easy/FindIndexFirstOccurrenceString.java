public class FindIndexFirstOccurrenceString {
    public int strStr(String haystack, String needle) {
        for (int i = 0; i < haystack.length(); i++) {
            if (checkOccurrence(haystack, needle, i)) {
                return i;
            }
        }
        return -1;
    }

    private boolean checkOccurrence(String haystack, String needle, int index) {
        for (int i = 0; i < needle.length(); i++) {
            if (index >= haystack.length()) {
                return false;
            }
            if (haystack.charAt(index) != needle.charAt(i)) {
                return false;
            }
            index++;
        }
        return true;
    }
}
