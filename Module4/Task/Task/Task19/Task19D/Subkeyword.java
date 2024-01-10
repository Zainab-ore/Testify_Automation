package Task.Task.Task19.Task19D;

import java.util.Scanner;

public class Subkeyword {
    public static void main(String[] args)
    {
        Subkeyword value = new Subkeyword();
        Scanner input = new Scanner(System.in);
            // Ask the user for a name
            System.out.print("Enter your name: ");
            String userName = input.nextLine();
            value.printName(userName);

            input.close();
        }

    private void printName(String userName) {
    }
}


