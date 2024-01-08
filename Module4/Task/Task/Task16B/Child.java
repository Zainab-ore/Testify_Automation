package Task.Task.Task16B;

// Child Class extending Parent
public class Child extends Parent {
    // Override Method 1 in the child class
    public static void main(String[] args) {
        // Creating an object of Child class
        Child childObject = new Child();

        // Calling overridden methods
        childObject.Man("Hello, MR.!");
        childObject.Woman("MRS");
    }

    public void Man(String value) {
        System.out.println("Child Method 1: " + value);
    }

    // Override Method 2 in the child class
    public void Woman(String value) {
        System.out.println("Child Method 2: " + value);
    }
}