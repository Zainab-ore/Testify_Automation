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

        driver.findElement(By.xpath("//input[@id='user-name']")).click();
        driver.findElement(By.xpath("//input[@id='user-name']")).sendKeys("standard_user");

        driver.findElement(By.xpath("//input[@id='password']")).click();
        driver.findElement(By.xpath("//input[@id='password']")).sendKeys("secret_sauce");

        driver.findElement(By.xpath("//input[@id='login-button']")).click();

        Thread.sleep(500);
        //click on add to cart
        driver.findElement(By.xpath("//button[@id='add-to-cart-sauce-labs-backpack']")).click();
        Thread.sleep(2000);

        driver.findElement(By.xpath("//span[contains(text(),'1')]")).click();
        Thread.sleep(2000);

        driver.findElement(By.xpath("//button[@id='checkout']")).click();
        Thread.sleep(500);


        driver.quit();
    }
}

