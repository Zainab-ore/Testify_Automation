package Task.Task.Task12;

import Task.Task.Task12.Aplus;

public class Bplus {
    public static void main(String[] args) {
        Aplus path = new Aplus();
        path.publicMethod();

        Bplus pathTwo = new Bplus();
        pathTwo.privateMethod();

    }

    private void privateMethod()
    {
        System.out.println("This method can only be accessed within Class B.");
    }

    public void accessPrivateMethod() {
        // Accessing private method within the class
        privateMethod();
    }
}