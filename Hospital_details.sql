create database Hospitaldetails;
use Hospitaldetails;

CREATE TABLE  HospitalPatient (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    AdmissionDate DATE,
    HospitalName VARCHAR(100),
    HospitalAddress VARCHAR(255),
    HospitalCity VARCHAR(100),
    HospitalState VARCHAR(15),
    HospitalZipCode VARCHAR(10)
);


DELIMITER //

CREATE PROCEDURE InsertMultiplePatients()
BEGIN
    DECLARE counter INT DEFAULT 0;
    
    WHILE counter < 200 DO
        INSERT INTO HospitalPatient (Name, Age, Gender, AdmissionDate, HospitalName, HospitalAddress, HospitalCity, HospitalState, HospitalZipCode)
        VALUES (
            CONCAT('Patient_', counter + 1),
            FLOOR(RAND() * 80) + 18,
            IF(RAND() < 0.5, 'Male', 'Female'),
            DATE_ADD('2024-01-01', INTERVAL FLOOR(RAND() * 365) DAY),
            IF(RAND()  < 0.5, 'Mayo Clinic','Johns Hopkins Hospital'),
            IF(RAND()  < 0.5 , ' Example St1',' Example st2'),
            IF(RAND() < 0.5, 'New York City' , 'Los Angeles'),
            IF(RAND() < 0.5, 'New york','California'),
            If(RAND() < 0.5, '12345','12347')
        );
        
        SET counter = counter + 1;
    END WHILE;
END //

DELIMITER ;

CALL InsertMultiplePatients();

select * from hospitalpatient;