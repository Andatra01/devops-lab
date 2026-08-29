const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

// Абсолютный путь к файлу внутри смонтированного тома
const DATA_FILE = '/opt/app/data/req';

// Обработчик для записи данных
app.get('/set', (req, res) => {
	try {
		// Создаём папку, если её нет (рекурсивно)
		fs.mkdirSync(path.dirname(DATA_FILE), { recursive: true });
		// Записываем значение из параметра id в файл
		fs.writeFileSync(DATA_FILE, req.query.id || '');
		res.send('done!');
	} catch (err) {
		console.error('Ошибка записи:', err);
		res.status(500).send('error');
	}
});

// Обработчик для чтения данных
app.get('/get', (req, res) => {
	try {
		// Читаем файл, если он существует
		const data = fs.readFileSync(DATA_FILE, 'utf8');
		res.send(data);
	} catch (err) {
		// Если файла нет или ошибка чтения, возвращаем пустую строку
		res.send('');
	}
});

// Запуск сервера
app.listen(port, () => {
	console.log(`server is listening on ${port}`);
});