Feature: Calculator App

  @android
  Scenario: Verify addition of two numbers
    Given User is on "calculator" homepage
    When User clicks on "3"
    And User clicks on operator "plus"
    And User clicks on "7"
    And User clicks on operator "equal"
    Then User verifies answer is "10"

  Scenario Outline: Verify mathematics operations
    Given User is on "calculator" homepage
    When User clicks on "<num1>"
    And User clicks on operator "<operator1>"
    And User clicks on "<num2>"
    And User clicks on operator "<operator2>"
    Then User verifies answer is "<result>"
    Examples:
      | num1 | num2 | operator1 | result | operator2 |
      | 5    | 4    | plus      | 9      | equal     |
      | 9    | 5    | minus     | 4      | equal     |
      | 6    | 2    | div       | 3      | equal     |
      | 5    | 4    | mul       | 20     | equal     |