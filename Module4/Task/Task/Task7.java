import java.util.*;
import java.io.*;
public class Task7 {
    public static void main(String[] args) {
        // Create a 2D array with 4 rows and 3 columns
        String[][] fruitArray = new String[4][3];

        //fruit array
        fruitArray[0][0] = "Apple";
        fruitArray[1][1] = "Banana";
        fruitArray[2][2] = "Cashew";
        fruitArray[3][1] = "Date";
        System.out.println("Fruits  Column1  Column2");

        // Display the 2D array
        displayArray(fruitArray);

    }


    // Function to show the result of the array
    private static void displayArray(String[][] array) {
        for (int row = 0; row < array.length; row++) {
            for (int col = 0; col < array[row].length; col++) {

                System.out.print(array[row][col] + "\t");
            }
            System.out.println();
        }
    }
}
