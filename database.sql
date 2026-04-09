CREATE DATABASE hr_system;
USE hr_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(200),
    role ENUM('admin','recruiter','candidate')
);

CREATE TABLE jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    recruiter_id INT
);

CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    job_id INT,
    resume VARCHAR(255),
    status VARCHAR(50) DEFAULT 'Applied',
    notes TEXT
);

CREATE TABLE interviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    application_id INT,
    date DATE,
    time TIME
);
