const http = require('http');
const fs = require('fs');

const database = process.argv[2];

function getStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
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

    let result = `Number of students: ${students.length}`;

    Object.keys(fields).forEach((field) => {
      result += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
    });

    return result;
  } catch (error) {
    return 'Cannot load the database';
  }
}

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/students') {
    res.end(`This is the list of our students\n${getStudents(database)}`);
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
