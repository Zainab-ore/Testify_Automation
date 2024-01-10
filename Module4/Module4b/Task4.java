package Module4.Module4b;

public class Task4 {
        public static void main(String[] args) {
            System.out.println("Print prime numbers between 1 and 100:");

            for (int i = 1; i <= 100; i++) {
                if (isPrime(i)) {
                    System.out.print(i + " ");
                }
            }
        }

        private static boolean isPrime(int number) {
            if (number <= 1) {
                return false; // 1 is not a prime number
            }

            for (int i = 2; i <= Math.sqrt(number); i++) {
                if (number % i == 0) {
                    return false;
                }
            }
            return true;
        }
    }

