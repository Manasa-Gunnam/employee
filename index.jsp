<%@ page language="java" %>
<html>
<head>
    <title>Employee Search</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
    <h2>Employee Search</h2>

    <form action="EmployeeServlet" method="post">
        <input type="text" name="emp_id" placeholder="Enter Employee ID" required>
        <br>
        <input type="submit" value="Search">
    </form>
</div>

</body>
</html>
