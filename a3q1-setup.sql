-- Written by Samantha Beilman as part of Q1 solution
CREATE TABLE students(
	student_id			    SERIAL, 
	first_name			    VARCHAR(255) 	NOT NULL, 
	last_name			    VARCHAR(255) 	NOT NULL,
	email 				    VARCHAR(255) 	NOT NULL UNIQUE, 
	enrollment_date			DATE 			DEFAULT CURRENT_DATE,
	PRIMARY KEY (student_id)
);

-- Provided by professor
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');