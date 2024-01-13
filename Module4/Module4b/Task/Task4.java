package org.example;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class Task4
{
    public static void main(String[] args) throws InterruptedException
    {
        System.setProperty("webdriver.chrome.driver","C:\\Users\\oreoluwa.hammed\\IdeaProjects\\SeleniumIntro\\src\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();

        driver.get("http://demo.guru99.com/");

        driver.findElement(By.xpath("//a[contains(text(),'Security Project')]")).click();
        driver.switchTo().alert().dismiss();
        //Thread.sleep(3000);
        driver.findElement(By.xpath("//*[@id=\"dismiss-button\"]/div/span")).click();;

        Thread.sleep(3000);
        //Enter UserId
        driver.findElement(By.xpath("//tbody/tr[1]/td[2]/input[1]")).click();

        driver.findElement(By.xpath("//tbody/tr[1]/td[2]/input[1]")).sendKeys("Zainab1");
        //Enter Password
        driver.findElement(By.xpath("//tbody/tr[2]/td[2]/input[1]")).click();
        driver.findElement(By.xpath("//tbody/tr[2]/td[2]/input[1]")).sendKeys("Pass123$");

        driver.close();
    }
}

