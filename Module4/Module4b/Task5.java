package Module4.Module4b;
import java.util.*;
public class Task5 {

        public static void main(String[] args) {
            String[] input = {"akka", "akak", "baab", "baba", "bbaa"};
            Map<String, List<String>> anagramBuckets = createAnagramBuckets(input);
            for (List<String> bucket : anagramBuckets.values()) {
                System.out.println(bucket);
            }
        }

        private static Map<String, List<String>> createAnagramBuckets(String[] words)
        {
            Map<String, List<String>> anagramBuckets = new HashMap<>();
            for (String word : words) {
                // Sort the characters of the word to create a key
                char[] charArray = word.toCharArray();
                Arrays.sort(charArray);
                String key = new String(charArray);
                anagramBuckets.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
            }
            return anagramBuckets;
        }
    }

