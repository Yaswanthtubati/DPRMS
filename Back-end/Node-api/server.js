const mongoose = require('mongoose');
const dotenv = require('dotenv');
dotenv.config({path : './config.env'})
const app = require('./index')

const DB = process.env.DATABASE.replace('<PASSWORD>',process.env.DATABASE_PASSWORD);

mongoose.connect(DB, {
    useNewUrlParser : true,
    useCreateIndex : true,
    useUnifiedTopology : true,
    useFindAndModify : false
}).then(() => {
    console.log('Database connected successfully')
});



const port = process.env.PORT || 3000

app.listen(port,() => {
    console.log(`Listening to the server at port ${port}`);
})
