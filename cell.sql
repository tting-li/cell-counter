-- project table:
CREATE TABLE projects (
    project_id VARCHAR(10) PRIMARY KEY, 
    project_name VARCHAR(200) NOT NULL,
    description TEXT,
);

-- subjects
CREATE TABLE subjects (
    subject_id VARCHAR(15)
    age INT,
    gender CHAR(10),
    project_id VARCHAR (10)
    UNIQUE(subject_id, project_id)
);

-- condition
CREATE TABLE conditions (
    condition_id VARCHAR(100),
    condition_name VARCHAR(50) UNIQUE,
    description TEXT
);

-- treatments
CREATE TABLE treatments (
    treatment_id VARCHAR(10) PRIMARY KEY,
    treatment_name VARCHAR(100),
    description TEXT
);

-- samples 
CREATE TABLE samples (
    sample_id VARCHAR(15) PRIMARY KEY,
    subject_id VARCHAR(15),
    sample_type_id VARCHAR(10),
    collection_date DATE,
    project_id VARCHAR(10),
    treatment_id VARCHAR(10),
    response CHAR(1),
    time_from_treatment_start INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (sample_type_id) REFERENCES sample_types(sample_type_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (treatment_id) REFERENCES treatments(treatment_id)
);

CREATE TABLE CellCounts (
    cell_counts VARCHAR(10) PRIMARY KEY,
    sample_id INT REFERENCES Samples(sample_id),
    cell_population VARCHAR(50), 
    count INT,
    percentage FLOAT
);




