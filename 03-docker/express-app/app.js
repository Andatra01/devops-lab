const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('OK'));
app.get('/health', (req, res) => res.json({status: 'ok'}));

app.listen(3000, () => console.log('Listening on 3000'));
