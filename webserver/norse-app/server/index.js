// server/index.js
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();
const PORT = 5000;


// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/norse', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

// Define a schema and model for the 'norsedata' collection
const norseDataSchema = new mongoose.Schema({}, { collection: 'norsedata' });
const NorseData = mongoose.model('NorseData', norseDataSchema);


// Define the /flights endpoint
app.get('/flights', async (req, res) => {
    console.log("test")
    try {
      const data = await NorseData.find({});
      res.json(data);
    } catch (err) {
      res.status(500).send(err);
    }
  });

app.use(cors());
app.use(bodyParser.json());

// Sample route
app.get('/api/data', (req, res) => {
    res.json({ message: 'Hello from the server!' });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
