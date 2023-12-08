import java.util.*;

public class Task8 {
    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt user for principal amount
        System.out.print("Enter the principal amount: ");
        double principal = scanner.nextDouble();

        // Prompt user for interest rate
        System.out.print("Enter the annual interest rate (in percentage): ");
        double Rate = scanner.nextDouble();

        // Prompt user for the time (in years)
        System.out.print("Enter the time (in years): ");
        double time = scanner.nextDouble();

        // Close the scanner to avoid resource leaks
        scanner.close();

        // Calculate simple interest
        double simpleInterest = (principal * Rate * time) / 100;

        // Communicate the result to the user
        System.out.println("Simple Interest Calculation: " );
        System.out.println("Principal Amount: ₦" + principal);
        System.out.println("Annual Interest Rate: " + Rate + "%");
        System.out.println("Time (in years): " + time + "years");
        System.out.println("Simple Interest: ₦" + simpleInterest);
    }
}
