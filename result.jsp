<%@ page language="java" %>
<html>
<head>
    <title>Employee Details</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="result-box">
    <h2>Employee Details</h2>

    <%
        if (request.getAttribute("message") != null) {
    %>
        <p class="error"><%= request.getAttribute("message") %></p>
    <%
        } else {
    %>
        <p><b>ID:</b> <%= request.getAttribute("emp_id") %></p>
        <p><b>Name:</b> <%= request.getAttribute("emp_name") %></p>
        <p><b>Department:</b> <%= request.getAttribute("department") %></p>
        <p><b>Salary:</b> ₹<%= request.getAttribute("salary") %></p>
        <p class="success">Record fetched successfully!</p>
    <%
        }
    %>

</div>

</body>
</html>
