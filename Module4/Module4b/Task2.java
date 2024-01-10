package Module4.Module4b;
public class Task2 {
    public static void main(String[] args) {

        String sentence = "I am the best AutomationTester";

        // Reverse the position of words using recursion
        String reversedSentence = reverseWords(sentence);

        // Print the original and reversed sentences
        System.out.println("Original Sentence: " + sentence);
        System.out.println("Reversed Sentence: " + reversedSentence);
    }
    private static String reverseWords(String sentence) {
        String[] words = sentence.split("\\s");
        reverseWordsArray(words, 0, words.length - 1);
        return String.join(" ", words);
    }

    private static void reverseWordsArray(String[] words, int start, int finish) {
        if (start < finish) {

            String stop = words[start];
            words[start] = words[finish];
            words[finish] = stop;
            reverseWordsArray(words, start + 1, finish - 1);
        }
    }
}