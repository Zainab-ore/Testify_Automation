package Task.Task.Task15;

// Child Class B
class B extends A {
    // Method 4 in class B
    public void method4()
    {
        System.out.println("Method 4 in class B");
    }
    // Method 5 in class B
    public void method5()
    {
        System.out.println("Method 5 in class B");
    }

    // Main method to invoke all 5 methods
    public static void main(String[] args) {
        // Creating an object of class B
        B objB = new B();

        // Invoking methods from class A
        objB.method1();
        objB.method2();
        objB.method3();

        // Invoking methods from class B
        objB.method4();
        objB.method5();
    }
}
