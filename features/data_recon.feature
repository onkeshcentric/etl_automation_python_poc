Feature: ETL Tests Data Recon
  Sample tests for ETL testing POC

  Scenario: Check count between source and destination
    Given I connect to source and destination databases
    Then I fetch count for "members" table from "source" database
    Then I fetch count for "reports" table from "destination" database
    Then I validate the count between tables "members" and "reports"



