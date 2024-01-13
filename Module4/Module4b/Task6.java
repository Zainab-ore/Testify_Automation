package Module4.Module4b;
import java.util.Arrays;
public class Task6 {
    public static void main(String[] args) {
        String inputString = "Despite commuting at peek hours, she was able to keep to time";
        String[] words = inputString.split("\\s");
        checkForAnagram(words);
    }

    private static void checkForAnagram(String[] words) {
        for (int i = 0; i < words.length - 1; i++) {
            for (int j = i + 1; j < words.length; j++) {
                if (areAnagrams(words[i], words[j])) {
                    System.out.println("Anagrams: " + words[i] + " and  " + words[j]);
                }
            }
        }
    }
    private static boolean areAnagrams(String letter1, String letter2) {
        // Remove spaces and convert to lowercase for comparison
        letter1 = letter1.replaceAll("\\s", "").toLowerCase();
        letter2 = letter2.replaceAll("\\s", "").toLowerCase();

        char[] charArray1 = letter1.toCharArray();
        char[] charArray2 = letter2.toCharArray();

        Arrays.sort(charArray1);
        Arrays.sort(charArray2);

        return Arrays.equals(charArray1, charArray2);
    }
}