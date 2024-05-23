// server/index.js
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());


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

// Define the schema for the prices collection
const priceSchema = new mongoose.Schema({
  origin: String,
  destination: String,
  date: String,
  prices: [
    {
      collectionTime: Date,
      premium: Number,
      economy: Number
    }
  ]
});

// Create the model
const Price = mongoose.model('Price', priceSchema);


app.get('/api/unique-routes', async(req, res) => {
  try {
  // Define the aggregation pipeline
  const pipeline = [
    {
        $group: {
            _id: {
                origin: "$origin",
                destination: "$destination"
            }
        }
    },
    {
        $project: {
            _id: 0,
            origin: "$_id.origin",
            destination: "$_id.destination"
        }
    }
  ];

  // Execute the aggregation query
  const results = await Price.aggregate(pipeline);
  console.log(results)
  res.json(results);
  return results;
  } catch (error) {
    console.error('Error retrieving unique origin-destination combinations:', error);
  } finally {
  }
});

app.get('/api/price-history', async (req, res) => {
  const { origin, destination, startDate, endDate } = req.query;

  try {
    // Define the aggregation pipeline
    const pipeline = [
      // Match documents based on origin, destination, and date range
      {
        $match: {
          origin,
          destination,
          date: { $gte: startDate, $lte: endDate }
        }
      },
      // Unwind the prices array to work with individual price entries
      { $unwind: "$prices" },
      // Sort by departure date and collection time in ascending order
      { $sort: { 'prices.economy.departureDate': 1, 'prices.collection_time': 1 } },
      // Group by departure date and push prices into an array
      {
        $group: {
          _id: "$prices.economy.departureDate",
          prices: { $push: "$prices" }
        }
      },
      // Project the final output
      {
        $project: {
          _id: 0,
          departureDate: "$_id",
          prices: {
            $map: {
              input: "$prices",
              as: "price",
              in: {
                isSaleFare: "$$price.economy.isSaleFare",
                fareTotal: "$$price.economy.fareTotal",
                timestamp: "$$price.economy.timestamp"
              }
            }
          }
        }
      },
      // Sort departure dates in ascending order
      { $sort: { departureDate: 1 } }
    ];

    // Execute the aggregation query
    const groupedPrices = await Price.aggregate(pipeline);
    console.log(groupedPrices[0].prices[0])
    console.log(groupedPrices[0].prices[1])

    // Send the grouped price history as JSON
    res.json(groupedPrices);
  } catch (error) {
    console.error('Error retrieving price history:', error);
    res.status(500).send('Internal Server Error');
  }
});
/*

app.get('/api/price-history', async (req, res) => {
  const { origin, destination, startDate, endDate } = req.query;

  try {
    // Define the aggregation pipeline
    const pipeline = [
      // Match documents based on origin, destination, and date range
      {
        $match: {
          origin,
          destination,
          date: { $gte: startDate, $lte: endDate }
        }
      },
      // Unwind the prices array to work with individual price entries
      { $unwind: "$prices" },
      // Sort by departure date and collection time in ascending order
      { $sort: { 'prices.economy.departureDate': 1, 'prices.collection_time': 1 } },
      // Group by departure date and push prices into an array
      {
        $group: {
          _id: "$prices.economy.departureDate",
          prices: { $push: "$prices" }
        }
      },
      // Project the final output
      {
        $project: {
          _id: 0,
          departureDate: "$_id",
          prices: 1
        }
      },
      // Sort departure dates in ascending order
      { $sort: { departureDate: 1 } }
    ];

    // Execute the aggregation query
    const groupedPrices = await Price.aggregate(pipeline);
    console.log(groupedPrices[0].prices[0])

    // Send the grouped price history as JSON
    res.json(groupedPrices);
  } catch (error) {
    console.error('Error retrieving price history:', error);
    res.status(500).send('Internal Server Error');
  }
});
*/

// Sample route
app.get('/api/data', (req, res) => {
    res.json({ message: 'Hello from the server!' });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
