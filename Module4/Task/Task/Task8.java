import java.util.*;

public class Task8 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Prompt user for principal amount
        System.out.print("Enter the principal amount: ");
        double principal = scanner.nextDouble();

        // Prompt user for interest rate
        System.out.print("Enter the annual interest rate (in percent): ");
        double Rate = scanner.nextDouble();

        System.out.print("Enter the time (in years): ");
        double time = scanner.nextDouble();

        // Calculate simple interest
        double simpleInterest = (principal * Rate * time) / 100;

        // print the result
        System.out.println("Simple Interest Calculation: " );
        System.out.println("Principal Amount: ₦" + principal);
        System.out.println("Annual Interest Rate: " + Rate + "%");
        System.out.println("Time (in years): " + time + "years");
        System.out.println("Simple Interest: ₦" + simpleInterest);
    }
}
