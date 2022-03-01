package hello.servlet.web.servletmvc;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet(name = "mvcMemberListServlet", urlPatterns = "/servlet-mvc/members")
public class MvcMemberListServlet extends HttpServlet {
    // 저장소 싱클톤 객체 꺼내기

    private MemberRepository memberRepository = MemberRepository.getInstance();

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("MvcMemberListServlet.service");

        List<Member> members = memberRepository.findAll();

        // HTTPServletRequest 객체 활용해서 MODEL 담기

        request.setAttribute("members", members);
        String viewPath = "/WEB-INF/views/members.jsp";

        // 컨트롤러가 외부 디렉토리에서 view 가지고 오기
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
        // view에 모델 전달하기
        dispatcher.forward(request, response);
    }
}