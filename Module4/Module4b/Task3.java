package Module4.Module4b;

public class Task3
{
        public static void main(String[] args) {
            int[] array = {1, 8, 9, 2, 10};

            if (array.length < 2) {
                System.out.println("Array should have at least two elements to find a pair with maximum product.");
            } else {
                findMaxProductPair(array);
            }
        }

        private static void findMaxProductPair(int[] array) {
            int max1 = Integer.MIN_VALUE;
            int max2 = Integer.MIN_VALUE;

            int min1 = Integer.MAX_VALUE;
            int min2 = Integer.MAX_VALUE;

            for (int num : array) {
                // Update the maximum values
                if (num > max1) {
                    max2 = max1;
                    max1 = num;
                } else if (num > max2) {
                    max2 = num;
                }

                // Update the minimum values
                if (num < min1) {
                    min2 = min1;
                    min1 = num;
                } else if (num < min2) {
                    min2 = num;
                }
            }

            if (max1 * max2 > min1 * min2) {
                System.out.println("Pair with maximum product: (" + max1 + ", " + max2 + ")");
            } else {
                System.out.println("Pair with maximum product: (" + min1 + ", " + min2 + ")");
            }
        }
    }

