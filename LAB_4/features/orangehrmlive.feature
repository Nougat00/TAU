# Created by Bartosz Laskowski at 17.12.2023
Feature: Changing username on orangehrmlive.com

  Scenario: Login to orangehrmlive.com and change username
    Given I am on the orangehrmlive.com login page
    When I enter username: "Admin" and password: "admin123"
    And I click login button
    Then I should be logged in successfully to orangehrmlive.com
    And I change my username to "Tester"
