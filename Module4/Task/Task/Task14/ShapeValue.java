package Task.Task.Task14;


public class ShapeValue {
    public static void main(String[] args) {
        // Creating an object of Class A
        ShapeSide square = new ShapeSide();
        // Setting values for length and breadth
        square.setShapeLength(10.0);
        square.setShapeBreadth(10.0);

        // Calculating the area of the square
        double area = square.getShapeLength() * square.getShapeBreadth();

        // Printing the final calculation
        System.out.println("The area of a square of length: " + square.getShapeLength() +
                " and breadth " + square.getShapeBreadth() + " is " + area);
    }
}

