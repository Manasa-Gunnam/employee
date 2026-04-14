import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;

public class EmployeeServlet extends HttpServlet {

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String empId = request.getParameter("emp_id");

        String url = "jdbc:mysql://localhost:3306/company_db";
        String user = "root";
        String password = "root"; // change if needed

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection(url, user, password);

            PreparedStatement ps = con.prepareStatement(
                "SELECT * FROM employee WHERE emp_id = ?"
            );

            ps.setInt(1, Integer.parseInt(empId));

            ResultSet rs = ps.executeQuery();

            if (rs.next()) {
                request.setAttribute("emp_id", rs.getInt("emp_id"));
                request.setAttribute("emp_name", rs.getString("emp_name"));
                request.setAttribute("department", rs.getString("department"));
                request.setAttribute("salary", rs.getDouble("salary"));
            } else {
                request.setAttribute("message", "Employee not found!");
            }

            RequestDispatcher rd = request.getRequestDispatcher("result.jsp");
            rd.forward(request, response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
