const express = require('express');
const cors = require('cors');
const mysql = require('mysql');
const multer  = require('multer');
const csv = require('csv-parser');
const fs = require('fs');


const Readable = require('stream').Readable; // used to convert the buffer to a stream

const upload = multer({ storage: multer.memoryStorage() }); // store files in memory

const app = express();
app.use(cors());

// create database connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root', // mysql user
  password: '', // mysql password
  database: 'projwifianalyzer' // database name
});

// connect to the database
db.connect((err) => {
  if (err) throw err;
  console.log('Connected to the database');
});

// endpoint to check is API is running 
app.get('/check', (req, res) => {
  res.json('API is running');
});

// endpoint to get data from your database
app.get('/items', (req, res) => {
  const sql = 'SELECT * FROM scans'; 
  db.query(sql, (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

// create new get to search users datable to match login
app.get('/login', (req, res) => {
  const sql = 'SELECT * FROM users WHERE username = ? AND password = ?'; 
  db.query(sql, [req.query.username, req.query.password], (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

app.get('/inspect', (req, res) => {
  const sql = 'SELECT * FROM scans WHERE scanID = ?'; 
  console.log(req.query.scanID)
  db.query(sql, [req.query.scanID], (err, results) => {
    if (err) throw err;
    res.json(results);
  }
  );
});

function clearEmptyLines(fileBuffer) {
  // Convert the file buffer to a string
  const fileContent = fileBuffer.toString('utf-8');

  // Split the content into lines
  const lines = fileContent.split('\n');

  // Remove empty lines
  const nonEmptyLines = lines.filter(line => line.trim() !== '');

  // Join the lines
  const updatedContent = nonEmptyLines.join('\n');

  // Convert the updated content back to a buffer
  const updatedBuffer = Buffer.from(updatedContent, 'utf-8');

  return updatedBuffer;
}

app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file was uploaded.');
  }

  req.file.buffer = clearEmptyLines(req.file.buffer);

  const results = [];
  const stream = Readable.from(req.file.buffer.toString());

  stream
    .pipe(csv())
    .on('data', (data) => results.push(data))
    .on('end', () => {
      // Process the results array
      results.forEach((result) => {
        // Process each result object
        const formattedData = {
          BSSID: result.BSSID,
          Firsttimeseen: result.Firsttimeseen,
          Lasttimeseen: result.Lasttimeseen,
          Channel: result.Channel,
          Speed: result.Speed,
          Privacy: result.Privacy,
          Cipher: result.Cipher,
          Authentication: result.Authentication,
          Power: result.Power,
          Beacons: result.Beacons,
          IV: result.IV,
          LANIP: result.LANIP,
          IDlength: result.IDlength,
          ESSID: result.ESSID,
          Key: result.Key,
          WPSVersion: result.WPSVersion,
          WPSState: result.WPSState,
          WPSlocked: result.WPSlocked,
          WPSmethod: result.WPSmethod,
          Manufacturer: result.Manufacturer,
        };

        const insertSql = 'INSERT INTO scans SET ?';
        db.query(insertSql, formattedData, (err, result) => {
          if (err) throw err;
          console.log('Data inserted');
        });
      });

      res.send('Data uploaded successfully.');
    })
    .on('error', (err) => {
      console.error(err);
      res.status(500).send('An error occurred during file processing.');
    });
});


const port = 3000;
app.listen(port, () => console.log(`Server is listening on port ${port}`));
