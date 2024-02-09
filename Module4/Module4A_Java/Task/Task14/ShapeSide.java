package Task.Task.Task14;
// Class A (Square Shape)
public class ShapeSide {
    public static void main(String[] args) {
        ShapeSide Shapes = new ShapeSide();
        Shapes.getShapeSides();
    int correctShape = Shapes.getShapeSides();
        System.out.println(correctShape);
}
    private int shapeSides = 4;
    private double shapeLength;
    private double shapeBreadth;

    // Getter for shape sides (Read-only)
    public int getShapeSides()
    {
        return shapeSides;
    }
    // Getter and Setter for shape length
    public double getShapeLength()
    {
        return shapeLength;
    }
    public void setShapeLength(double length) {
        if (length > 0) {
            this.shapeLength = length;
        } else {
            System.out.println("Invalid length value. Length must be greater than 0.");
        }
    }

    // Getter and Setter for shape breadth
    public double getShapeBreadth()
    {
        return shapeBreadth;
    }

    public void setShapeBreadth(double breadth) {
        if (breadth > 0) {
            this.shapeBreadth = breadth;
        } else {
            System.out.println("Invalid breadth value. Breadth must be greater than 0.");
        }
    }
}
