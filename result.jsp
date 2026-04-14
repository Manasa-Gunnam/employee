<%@ page language="java" %>
<html>
<head>
    <title>Result</title>
</head>
<body>

<h2>Employee Details</h2>

<%
    if (request.getAttribute("message") != null) {
%>
        <h3><%= request.getAttribute("message") %></h3>
<%
    } else {
%>
        <p>ID: <%= request.getAttribute("emp_id") %></p>
        <p>Name: <%= request.getAttribute("emp_name") %></p>
        <p>Department: <%= request.getAttribute("department") %></p>
        <p>Salary: <%= request.getAttribute("salary") %></p>
<%
    }
%>

</body>
</html>
