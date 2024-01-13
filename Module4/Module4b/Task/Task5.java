package org.example;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class Task5
{
    public static void main(String[] args) throws InterruptedException
    {
        System.setProperty("webdriver.chrome.driver","C:\\Users\\oreoluwa.hammed\\IdeaProjects\\SeleniumIntro\\src\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        //launch URl
        driver.get("https://www.saucedemo.com/");

        //Enter UserId
        driver.findElement(By.xpath("//input[@id='user-name']")).click();
        driver.findElement(By.xpath("//input[@id='user-name']")).sendKeys("visual_user");
        //Enter Password
        driver.findElement(By.xpath("//input[@id='password']")).click();
        driver.findElement(By.xpath("//input[@id='password']")).sendKeys("secret_sauce");

        //click on the login button
        driver.findElement(By.xpath("//input[@id='login-button']")).click();

        Thread.sleep(500);
        //click on Add to cart
        driver.findElement(By.xpath("//button[@id='add-to-cart-sauce-labs-backpack']")).click();
        Thread.sleep(2000);

        //Click on cart icon
        driver.findElement(By.xpath("//span[contains(text(),'1')]")).click();
        Thread.sleep(1000);

        //Click on Checkout
        driver.findElement(By.xpath("//button[@id='checkout']")).click();
        Thread.sleep(500);


        driver.quit();
    }
}

