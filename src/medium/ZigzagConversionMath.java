package medium;

public class ZigzagConversionMath {
    public static void main(String[] args) {
        System.out.println(new ZigzagConversionMath().convert("ABCDEFGHIJKLMNOP", 5));
        System.out.println(new ZigzagConversionMath().convert("ABCDEFGHIJKLMNOP", 1));
    }

    /**
    /   A         I
         B       H J     P
          C     G   K   O
           D  F      L N
            E         M

     AI BHJP CGKO DFLN EM
     */

    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }

        StringBuilder stringBuilder = new StringBuilder();
        int steps = 2 * (numRows - 1);
        for (int startIndex = 0; startIndex < numRows; startIndex++) {
            int i = startIndex;
            int minorStep = 2 * (numRows - startIndex - 1);
            while (i < s.length()) {
                stringBuilder.append(s.charAt(i));
                if (startIndex > 0 && startIndex < numRows - 1 && i + minorStep < s.length()) {
                    stringBuilder.append(s.charAt(i + minorStep));
                }
                i += steps;
            }
        }
        return stringBuilder.toString();
    }
}
