CREATE TABLE tbr (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genres VARCHAR(255) NOT NULL,   -- multiple genres separated by commas
    status VARCHAR (50) NOT NULL,
    author VARCHAR(50),
    page_count INT,
    start_date DATE,
    end_date DATE,
    skipped BOOLEAN DEFAULT FALSE,  -- track if the book has been skipped
    DNF BOOLEAN DEFAULT FALSE,  -- track if not continuing 
    rating DECIMAL,
    notes VARCHAR(255)
);
