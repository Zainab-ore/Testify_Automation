package Task.Task.Task12;

import Task.Task.Task12.Bplus;

// Class A in Package1
public class Aplus {
    /**
     *
     */
    public static void main(String[] args) {
        Aplus path = new Aplus();

        path.publicMethod();
    }

    // Public method accessible anywhere in the project
    public void publicMethod()
    {
        System.out.println("This method can be accessed anywhere in the project.");
    }
}
