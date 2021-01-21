# ETL Automation POC using Python
ETL Automation POC using Python

## BDD Approach
Implemented using behave
To execute all the BDD scenarios in the framework, simply use the command: `behave`

To execute specific feature file, use the command: 

`behave <relative path to feature file>:<scenario line number>`

### ETL Scenarios categories implemented
- Data Conformance
- Data Reconciliation
- Data Transformation

### Reporting

Current reporting is being done using allure reports.
The execution command changes into: 

`behave -f allure_behave.formatter:AllureFormatter -o reports ./features`

To view the reports, execute the following command: `allure serve reports`