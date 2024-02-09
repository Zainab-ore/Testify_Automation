package org.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class GoogleNavigate
{
    public static void main(String[] args)
    {
        System.setProperty("webdriver.chrome.driver","C:\\Users\\oreoluwa.hammed\\IdeaProjects\\SeleniumIntro\\src\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://www.google.com/");
        driver.findElement(new By.ByLinkText("Sign in")).click();
        // driver.findElement(By.name("q")).sendKeys("HAMMED OREOLUWA ZAINAB");
    }
}
