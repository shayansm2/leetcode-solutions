package medium;

import java.util.HashMap;
import java.util.Map;

public class ZigzagConversion {
    public String convert(String s, int numRows) {
        int row = 1;
        int direction = 1;
        Map<Integer, String> lines = new HashMap<>();
        for (int i = 1; i <= numRows; i++) {
            lines.put(i, "");
        }
        for (char c : s.toCharArray()) {
            lines.put(row, lines.get(row) + c);
            if (numRows == 1) {
                continue;
            }
            if (direction == 1 && row == numRows) {
                direction = -1;
            } else if (direction == -1 && row == 1) {
                direction = 1;
            }
            row += direction;
        }

        StringBuilder result = new StringBuilder();
        for (int i = 1; i <= numRows; i++) {
            result.append(lines.get(i));
        }
        return result.toString();
    }
}
