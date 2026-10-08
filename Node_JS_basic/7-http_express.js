const express = require('express');
const fs = require('fs');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  fs.readFile(database, 'utf8', (error, data) => {
    if (error) {
      res.status(500).send('Cannot load the database');
      return;
    }

    const lines = data.trim().split('\n').filter((line) => line.trim());
    const students = lines.slice(1);
    const fields = {};

    students.forEach((student) => {
      const columns = student.split(',');
      const firstName = columns[0];
      const field = columns[3];

      if (!fields[field]) fields[field] = [];
      fields[field].push(firstName);
    });

    let result = `This is the list of our students\nNumber of students: ${students.length}`;

    Object.keys(fields).forEach((field) => {
      result += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
    });

    res.send(result);
  });
});

app.listen(1245);

module.exports = app;
