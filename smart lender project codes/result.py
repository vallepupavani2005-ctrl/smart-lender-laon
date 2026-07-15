<!DOCTYPE html>
<html>
<head>
    <title>Loan Result</title>

    <style>
        body{
            font-family:Arial;
            text-align:center;
            background:linear-gradient(to right, #ece9e6, #ffffff);
        }

        .box{
            margin-top:120px;
            display:inline-block;
            padding:40px;
            border-radius:15px;
            background:white;
            box-shadow:0px 0px 20px rgba(0,0,0,0.2);
        }

        h1{
            color:green;
            font-size:28px;
        }

        a{
            display:inline-block;
            margin-top:20px;
            padding:10px 20px;
            background:#007bff;
            color:white;
            text-decoration:none;
            border-radius:8px;
        }

        a:hover{
            background:#0056b3;
        }
    </style>

</head>

<body>

    <div class="box">

        <!-- 👉 Flask nunchi vachina output -->
        <h1>{{ result }}</h1>

        <!-- 👉 back button -->
        <a href="/">Try Again</a>

    </div>

</body>
</html>