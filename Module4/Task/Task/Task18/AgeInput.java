package Task.Task.Task18;

import java.util.InputMismatchException;
import java.util.Scanner;

public class AgeInput {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        try {
            // Ask the user for age
            System.out.print("Enter your age: ");
            int age = input.nextInt();

            // Print the entered age
            System.out.println("The date entered is: " + age+ "years");
        }
        catch (InputMismatchException e)
        {
            // Handle the exception when the user enters a value that is not of integer data type.
            System.out.println("Error: Invalid information supplied. Please enter a valid number for age.");

        }
    }
}

