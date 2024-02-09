package org.example;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class Task8
    {
        public static void main(String[] args) throws InterruptedException {
            System.setProperty("webdriver.chrome.driver", "C:\\Users\\oreoluwa.hammed\\IdeaProjects\\SeleniumIntro\\src\\chromedriver.exe");
            WebDriver driver = new ChromeDriver();
            driver.manage().window().maximize();


        }
}
