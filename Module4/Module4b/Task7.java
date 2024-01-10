package Module4.Module4b;

public class Task7 {
        public static void main(String[] args) {
            String word = "TestifyAutomation";
            String reversedString = reverseString(word);
            System.out.println("Original String: " + word);
            System.out.println("Reversed String: " + reversedString);
        }

        // Function to reverse a string using recursion
        private static String reverseString(String letter) {
            // Base case: return the string if it's empty or contains only one character
            if (letter == null || letter.length() <= 1) {
                return letter;
            }
            // Recursive call to reverse the substring excluding the first character
            String reversedSubstring = reverseString(letter.substring(1));
            // Concatenate the first character with the reversed substring
            return reversedSubstring + letter.charAt(0);
        }
    }

