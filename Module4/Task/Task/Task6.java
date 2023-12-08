import java.util.*;
import java.io.*;

public class Task6 {
    public static void main(String[] args) {
        //the original string
        String originalString = "DEMOCRACY";

        // To reverse the string
        String reversedString = reverseString(originalString);

        // To extract the word "COME" from the reversd string
        String extractedWord = extractWord(reversedString);

        // Display all results
        System.out.println("Original String: " + originalString);
        System.out.println("Reversed String: " + reversedString);
        System.out.println("Extracted Word:  " + extractedWord);
    }

    // Create a function to reverse the string
    public static String reverseString(String word) {
        StringBuilder stringBuilder = new StringBuilder(word);
        stringBuilder.reverse();

        return stringBuilder.toString();
    }

    // Function to extract a specific word from a string
    private static String extractWord(String word) {
        if (word.contains("COME")) {
            return "COME";
        } else {


            return "invalid";
        }
    }
}


