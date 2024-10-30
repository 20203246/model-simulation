package lesson1;
import jakarta.servlet.*;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.*;

public class _01_getJDBC implements Servlet{
    private ServletConfig servletConfig = null;
    @Override
    public void init(ServletConfig servletConfig) throws ServletException {
        System.out.println("_01获取JDBC内容并返回结果 init method execute!");
        this.servletConfig = servletConfig;
    }

    @Override
    public ServletConfig getServletConfig() {
        return servletConfig;
    }

    /**
     * 一个路径代表一个资源，这个资源可能是静态资源也可能是一个动态资源（Java小程序）
     */
    @Override
    public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
        System.out.println("_01_getJDBC init method execute!");

        servletResponse.setContentType("text/html;charset=UTF-8");

        PrintWriter out = servletResponse.getWriter();

        ResultSet rs = null;
        PreparedStatement ps = null;
        Connection conn = null;

        try{
            // 注意：还要在WEB/lib下放置jar包
            Class.forName("com.mysql.cj.jdbc.Driver"); // 注册驱动
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test",
                    this.getServletConfig().getInitParameter("MysqlName"),
                    this.getServletConfig().getInitParameter("MysqlPasswd"));
            String sql = "select no,name from t_student";
            ps = conn.prepareStatement(sql);
            rs = ps.executeQuery();
            while(rs.next()){
                String no = rs.getString("no");
                String name = rs.getString("name");
                out.print(no+","+name+"<br>");
            }
        }catch(ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (ps != null) {
                try {
                    ps.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }


    }

    @Override
    public String getServletInfo() {
        return "";
    }

    @Override
    public void destroy() {

    }
}
