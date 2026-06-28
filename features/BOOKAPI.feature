Feature: Verify if books are added and deleted using library API
   @library
  Scenario: Verify AddBook API functionality
      Given the Book details which needs to be added to library
      When we execute the AddBook Post method
      Then book is successfully added
     And status code of response should be 200

   @library
   Scenario Outline: Verify AddBook API functionality   #for parameterization this outline is important this is how we data driven with parameters
      Given the Book details with <isbn> and <aisle>
      When we execute the AddBook Post method
      Then book is successfully added
     Examples:
       | isbn  | aisle |
       | sdsfg | 4465  |
       | adafa | 54652 |


  #. --no-capture
  #
  #By default, Behave captures print statements / console output and hides them unless a test fails.
  #
  #With:
#& "C:\allure-2.43.0\allure-2.43.0\bin\allure.bat" serve AllureReports - to see html reports