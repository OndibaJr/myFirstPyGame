-- Create a sample table
CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);

-- Insert some sample data
INSERT INTO Employees (ID, FirstName, LastName, Department, Salary)
VALUES
(1, 'John', 'Doe', 'Finance', 50000.00),
(2, 'Jane', 'Smith', 'HR', 60000.00),
(3, 'Mike', 'Johnson', 'IT', 75000.00);

-- Retrieve all records
SELECT * FROM Employees;

-- Optional: Update a record
UPDATE Employees
SET Salary = 80000.00
WHERE ID = 3;

-- Retrieve updated records
SELECT * FROM Employees;

-- Optional: Delete a record
DELETE FROM Employees
WHERE ID = 1;

-- Final table view
SELECT * FROM Employees;
