package org.example;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Task7 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver",
                "C:\\Users\\oreoluwa.hammed\\IdeaProjects\\SeleniumIntro\\src\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://worldweather.wmo.int/en/home.html");
        Thread.sleep(10000);

        driver.findElement(By.xpath("//input[@type='text']")).click();
        driver.findElement(By.xpath("//input[@type='text']")).sendKeys("Abuja");
        driver.findElement(By.xpath("//input[@name='submit']")).click();

        String weatherRep;
        weatherRep = By.xpath("/html/body/div[1]/div[6]/div[5]/div[2]").findElement(driver).getText();
        Thread.sleep(2000);
        System.out.println(weatherRep);

        driver.quit();
    }
}
