const port=4000;

const express=require("express");
const app=express();
const mongoose=require('mongoose')
const jwt=require("jsonwebtoken");
const cors=require('cors');
const multer=require("multer")
const path=require("path")

app.use(express.json())
app.use(cors())

// Database Connection with mongoDB 
mongoose.connect("mongodb+srv://vishalkumar09837:Vishal03578106@cluster0.wi9rvw9.mongodb.net/ECOMMERCE");
//api creation
app.get("/",(req,res)=>{
    res.send("Express app is running")

})

const storage = multer.diskStorage({
    destination: './upload',
    filename: (req, file, cb) => {
        return cb(null, `${file.fieldname}_${Date.now()}${path.extname(file.originalname)}`);
    }
});
const upload = multer({ storage: storage });
app.use('/image',express.static('upload/images'))
app.post('/upload',upload.single('product'),(req,res)=>{
    app.json({
        success:1,
        image_url:`http://localhost:${port}/images/${req.file.filename}`
    })
})




app.listen(port,(error)=>{
    if(!error){
        console.log("Server is running on port "+port)
    }
    else{
        console.log("Error in running the server")
    }
})
