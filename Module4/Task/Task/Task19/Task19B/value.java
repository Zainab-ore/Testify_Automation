package Task.Task.Task19.Task19B;

// Class B
public class value {
    public static void main(String[] args)
    {
        // Setting the shareValue from Class A
        System.out.println("Shared value from class A in main method: " + Task.Task.Task19.Task19B.shareValue.sharedValues);

        // Changing the static variable from class A
        Task.Task.Task19.Task19B.shareValue.sharedValues = 50;

        // Creating an object of class B
        value secondObject = new value();
        // Calling a method in class B that prints the shared value
        secondObject.printSharedValues();
    }


    public void printSharedValues()
    {
        System.out.println("value from class A in class B: " + Task.Task.Task19.Task19B.shareValue.sharedValues);
    }
}
