<%@ page language="java" %>
<html>
<head>
    <title>Employee Search</title>
</head>
<body>

<h2>Enter Employee ID</h2>

<form action="EmployeeServlet" method="post">
    Employee ID: <input type="text" name="emp_id" required>
    <input type="submit" value="Search">
</form>

</body>
</html>
