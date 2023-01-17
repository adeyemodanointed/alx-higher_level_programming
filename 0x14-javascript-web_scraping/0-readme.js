#!/usr/bin/node

const request = require('request');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (error, data) => {
	if (error)
		console.log(error);
	if (data)
		console.log(data)
})
