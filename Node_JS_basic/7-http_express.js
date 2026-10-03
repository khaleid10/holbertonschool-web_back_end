const express = require('express');
const fs = require('fs');

const app = express();
const database = process.argv[2];

function getStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const fields = {};

      students.forEach((student) => {
        const columns = student.split(',');
        const firstName = columns[0];
        const field = columns[3];

        if (!fields[field]) fields[field] = [];
        fields[field].push(firstName);
      });

      const output = [`Number of students: ${students.length}`];

      Object.keys(fields).forEach((field) => {
        output.push(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      });

      resolve(output.join('\n'));
    });
  });
}

app.get('/', (req, res) => {
  res.type('text').send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const result = await getStudents(database);
    res.type('text').send(`This is the list of our students\n${result}`);
  } catch (error) {
    res.type('text').send(error.message);
  }
});

app.listen(1245);

module.exports = app;
