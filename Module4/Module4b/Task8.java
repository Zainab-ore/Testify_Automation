package Module4.Module4b;

import java.util.Arrays;

public class Task8 {
        public static void main(String[] args) {
            int[] numbers = {3,9,1,4,2,5,6,7,8};
            countingSort(numbers);
            System.out.println("Sorted Array: " + Arrays.toString(numbers));
        }

        // Counting sort function
        private static void countingSort(int[] arr) {
            int max = Arrays.stream(arr).max().orElse(0);
            int[] count = new int[max + 1];
            for (int number : arr) {
                count[number]++;
            }
            // Update the array with sorted values
            int index = 0;
            for (int i = 1; i <= max; i++) {
                while (count[i] > 0) {
                    arr[index++] = i;
                    count[i]--;
                }
            }
        }
    }
