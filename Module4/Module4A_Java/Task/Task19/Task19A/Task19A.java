package Task.Task.Task19.Task19A;// Class A

public class Task19A {
    public static void main(String[] args) {

    }

    // Variables
    private final int ballSize; // Using 'final' to make it unchangable
    private String ballColour;
    private String ballTexture;

    // Constructor
    public Task19A(int ballSize, String ballColour, String ballTexture) {
        this.ballSize = ballSize;
        this.ballColour = ballColour;
        this.ballTexture = ballTexture;
    }

    // Getter for ballSize (No setter to make it unmodifiable)
    public int getBallSize() {
        return ballSize;
    }

    public String getBallColour() {
        return ballColour;
    }
    public void setBallColour(String ballColour) {
        this.ballColour = ballColour;
    }
    public String getBallTexture() {
        return ballTexture;
    }
    public void setBallTexture(String ballTexture) {
        this.ballTexture = ballTexture;
    }
}
