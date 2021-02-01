DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS cart;

CREATE TABLE item (
  id INTEGER PRIMARY KEY,
  name TEXT,
  price REAL
);

INSERT INTO item (id, name, price) VALUES
  (1, 'AirSense 10 AutoSet for Her CPAP Machine', 22.0),
  (2, 'Opus 360 Nasal Pillow CPAP Mask with Headgear', 12.0),
  (3, 'AirFit F20 Full Face CPAP Mask with Headgear', 32.0),
  (4, 'AirFit F20 Full Face CPAP Mask with Headgear', 10.0),
  (5, 'AirFit P10 Nasal Pillows CPAP Mask System with Headgear', 55.0),
  (6, 'AirFit P10 Nasal Pillows CPAP Mask System with Headgear', 5.0),
  (7, 'AirSense 10 AutoSet CPAP Machine with HumidAir Heated Humidifier and SlimLine Tubing', 50.0),
  (8, 'AirSense 10 AutoSet CPAP Machine with HumidAir Heated Humidifier and SlimLine Tubing', 45.0);

CREATE TABLE cart (
  item_id INTEGER,
  quantity INTEGER,
  FOREIGN KEY (item_id) REFERENCES item (id),
  UNIQUE (item_id)
);
