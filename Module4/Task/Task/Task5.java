public class Task5
{
    public static void main(String [] args)
    {


        for(int number=1; number<=100; number++) {
            if (number % 5 == 0 && number % 3 == 0)
            {
                System.out.println("frizz buzz");
            }
            else if (number % 3 == 0)
            {
                System.out.println("fizz");
            }
            else if (number % 5 == 0)
            {
                System.out.println("buzz");
            }
            else
            {
                System.out.println(number);
            }
        }

    }
}
