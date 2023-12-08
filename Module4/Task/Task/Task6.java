import java.util.*;
import java.io.*;

public class Task6
{
    public static void main(String[] args)
    {
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
    private static String reverseString(String word) {
        return new StringBuilder(word).reverse().toString();
    }

    // Function to extract a specific word from a string
    private static String extractWord(String word) {
        int startIndex = word.indexOf("EMOC");
        int endIndex = startIndex + "EMOC".length();
        return word.substring(startIndex, endIndex);
    }
}


