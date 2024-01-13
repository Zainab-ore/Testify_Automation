package Task.Task.Task17B;
public class Loginpage implements Logintest {
    @Override
    public void testUsername(String username) {
        System.out.println("Verify that the " + username + "is valid");

    }
    @Override
    public void testPassword(String password) {
        System.out.println("Verify that  " + password + "is valid");

    }
    @Override
    public void testSuccessfulLogin(String username, String password) {
        System.out.println("Verify that login with  " + username + "&" + password + "is successful");

    }
}