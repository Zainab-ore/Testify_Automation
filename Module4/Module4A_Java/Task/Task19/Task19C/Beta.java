package Task.Task.Task19.Task19C;
import Task.Task.Task19.Task19C.*;

// Class Beta extending Class A
class Beta extends Alpha {
    String name = "Anderson";

    // This method uses super to access the name variable from Class A
    public void printBothNames() {
        super.printName(); // Accessing the printName method from Class A
        System.out.println("Other name from Class Beta: " + name);
    }
}



