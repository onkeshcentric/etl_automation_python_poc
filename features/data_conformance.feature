Feature: ETL Tests Data Conformance
  Sample tests for ETL testing POC


    Scenario: Check distinct count
    Given I connect to source and destination databases
    Then I fetch distinct count for "ID" in "members" table from "source" database
    Then I fetch distinct count for "ID" in "reports" table from "destination" database
    Then I validate the distinct count between tables "members" and "reports"



