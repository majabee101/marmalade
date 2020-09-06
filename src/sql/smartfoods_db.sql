CREATE TABLE Users (
    UserId int IDENTITY(1,1) PRIMARY KEY NOT NULL,
    UserName varchar(255) NOT NULL,
    FirstName varchar(255),
    LastName varchar(255),
    AddressLine1 varchar(255),
    AddressLine2 varchar(255),
    PostCode varchar(255)
)
INSERT INTO Users(UserName, FirstName, LastName, AddressLine1, AddressLine2, PostCode)
VALUES('Sami', 'Sami', 'Smith', 'Mariner Valley', 'Mars', 'MA1 1JS')
SELECT * FROM Users

CREATE TABLE Budgets (
    BudgetId int IDENTITY(1,1) PRIMARY KEY NOT NULL,
    Budget float(2),
    UserId int FOREIGN KEY REFERENCES Users(UserId) NOT NULL
)

INSERT INTO Budgets(Budget, UserId) VALUES(350.00, 1) 

SELECT * FROM Users
SELECT * FROM Budgets

SELECT a.UserName, b.Budget
FROM Users a 
INNER JOIN Budgets b ON a.UserId = b.UserId