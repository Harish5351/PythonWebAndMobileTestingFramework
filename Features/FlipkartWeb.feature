Feature: Flipkart web Testing

  Scenario: Verifying add to cart functionality working as expected
    Given User is on "flipkart" homepage
    When User clicks "LoginButton" on page
    And User enters "text" into text field
    Then User verifies "pagination_result" displayed
    When User clicks on "element" of page to compare elements
    Then User verifies "item" in tray
    When User clicks "COMPARE" on page
    Then User verifies "Items" displayed on screen
    When User navigates back to the previous page
    And User scroll down to "required_element" element
    And User navigates to product description window
    And User capture price of product
    And User clicks "AddToCart" on page
    And User navigates back to the previous page
    Then User verifies "GoToCart" displayed on screen
    When User clicks "GoToCart" on page
    Then User verifies "PLACE_ORDER" displayed on screen
    And User verifies "values" are the same before and after adding to the cart
    When User clicks "+" on page
    Then User verifies popup message "pup_up_message" displayed on screen
    When User clicks "remove" on page
    Then User verifies "Remove" displayed on screen
    And User verifies "Cancel" displayed on screen
    When User clicks "Remove" on page
    Then User verifies "MissingCartItems" displayed on screen
    And User verifies "ItemsAddedMessage" displayed on screen
    Then User verifies "Login" displayed on screen
