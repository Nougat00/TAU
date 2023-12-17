# Created by Bartosz Laskowski at 17.12.2023
Feature: Shopping on saucedemo.com

  Scenario: Login to saucedemo.com and add products to the cart
    Given I am on the saucedemo.com login page
    When I enter username "problem_user" and password "secret_sauce"
    And I click the login button
    Then I should be logged in successfully
    And I add products to the cart