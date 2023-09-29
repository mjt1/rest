//creating a simple express app
const express = require('express');
const app = express();
const PORT = 3000;

app.listen(PORT, () => {
    console.log('Server running at http://localhost:${PORT}');
});

//defining API Endpoints for managing Users
let users = [
    {id: 1, name: 'Alice'},
    {id:2, name: 'Bob'},
];

app.get('/users', (req, res) => {
    res.json(users);
});

app.get('/users/:id',(req, res) =>{
    const userId = parseInt(req.params.id);
    const user = users.find(user => user.id === userId);

    if (user) {
        res.json(user);
    }else {
        res.status(404).json({message:'User not found'});
    }
});

app.post('/users', express.json(), (req, res) => {
    const newUser =req.body;
    users.push(newUser);
    res.status(201).json(newUser);
});

app.put('/users/:id', express.json(), (req, res) =>{
    const userID = parseInt(req.params.id);
    const updatedUser = req.body;

    users = users.map(user => (user.id === userId ? {...user, ...updateUser }: user));
    res.json(updatedUser);
});

app.delete('/users/:id', (req, res) => {
    const userId = parseInt(req.params.id);
    users = users.filter(user => user.id !== userId);
    res.json({message:'User deleted'});
});
