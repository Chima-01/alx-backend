import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.hset('ALX', 'Portland', 50, print);
client.hset('ALX', 'Seattle', 80, print);
client.hset('ALX', 'New York', 20, print);
client.hset('ALX', 'Bagotay', 20, print);
client.hset('ALX', 'Paris', 2, print);

const data = client.hgetall('ALX', (err, data) => {
  err ? console.log(err) : console.log(JSON.stringify(data, null, 2));
});
