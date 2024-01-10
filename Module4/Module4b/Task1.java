package Module4.Module4b;

public class Task1 {
    public static void main(String[] args) {
        // To verify if "racecar" is a palindrome
        String word1 = "racecar";
        boolean isPalindrome1 = result(word1);
        System.out.println("\"" + word1 + "\" is a palindrome: " + isPalindrome1);

        // To verify if "10801" is a palindrome
        String word2 = "10801";
        boolean isPalindrome2 = result(word2);
        System.out.println("\"" + word2 + "\" is a palindrome: " + isPalindrome2);
    }
    // Function to check if the string is a palindrome
    public static boolean result(String letter)
    {
        letter = letter.replaceAll("\\s", "").toLowerCase();
        return letter.contentEquals(new StringBuilder(letter).reverse());
    }
}