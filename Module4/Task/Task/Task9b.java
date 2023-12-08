import java.util.Scanner;

public class Task9b {
    public static void main(String[] args) {

        verifyVisitor();
    }

    // Method to verify if visitors are coming for training
    private static void verifyVisitor() {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the visitor to enter a message
        System.out.print("Visitor, enter your message: ");
        String visitorMessage = scanner.nextLine();

        // Check if the visitor wrote "Testify"
        if (visitorMessage.equalsIgnoreCase("Testify")) {
            // Welcome message if they are coming for training
            System.out.println("Welcome! We are glad you are here for testify training.");
        } else {
            // Rejection message if they didn't write "Testify"
            System.out.println("Sorry, your presence is not for testifytraining. Rejected!");
        }

        // Close the scanner to avoid resource leaks
        scanner.close();
    }
}
