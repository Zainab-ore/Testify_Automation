import java.util.Scanner;
public class task10 {
    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter input
        String userInput;
        do {
            System.out.print("Enter a word (type 'testify' to exit): ");
            userInput = scanner.nextLine();

            // Check if the entered word is not "testify"
            if (!userInput.equalsIgnoreCase("testify")) {
                System.out.println("Try again.");
            }

        } while (!userInput.equalsIgnoreCase("testify"));

        // Close the scanner to avoid resource leaks
        scanner.close();

        // Print a message when "testify" is entered
        System.out.println("You entered 'testify'. Exiting the loop.");
    }
}
