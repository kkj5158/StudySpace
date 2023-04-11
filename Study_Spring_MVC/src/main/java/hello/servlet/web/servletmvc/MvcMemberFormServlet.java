package hello.servlet.web.servletmvc;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

 /*
      서블릿은 오직 컨트롤러만 역할을 한다, -> view는 다른 패키지에 있는 jsp 파일이 담당한다.
         */


@WebServlet(name = "mvcMemberFormServlet", urlPatterns = "/servlet-mvc/members/new-form")
public class MvcMemberFormServlet extends HttpServlet {

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        String viewPath = "/WEB-INF/views/new-form.jsp";

         /*
        view 를 연겷한다.
         */

        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);

       /*
       http 메소드를 연결한다.
       다른 서블릿이나 JSP로 이동할수 있는 기능 -> forward 서버 내부에서 다시 호출이 발생한다.
        */

        /*
        다음과 같은 MVC 패턴에서는 다음의 코드가 중복되어서 나타난다. -> mvc 패턴의 한계 // 이런 파일이 수백개 된다고 생각하면 중복은 수천개가 될것이다.

         */

        dispatcher.forward(request, response);

        /*
        /WEB-INF/ 이 경로안에 JSP 가 있으면 외부에서 직접 JSP 를 호출할 수 없다. 우리가 기대하는 것은 항상 컨트롤러를 통해서 JSP 를 호출하는 것이다.
         */

    }
}
