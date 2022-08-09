CREATE TABLE IF NOT EXISTS todo(
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(50),
    iscomplete INT DEFAULT 0
);

INSERT INTO todo (item) VALUE ("Mango");
INSERT INTO todo (item) VALUE ("Orange");
INSERT INTO todo (item) VALUE ("Pineaple");
INSERT INTO todo (item) VALUE ("Peach");
