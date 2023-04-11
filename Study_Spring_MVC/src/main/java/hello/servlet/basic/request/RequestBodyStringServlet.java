package hello.servlet.basic.request;

import org.springframework.util.StreamUtils;

import javax.servlet.ServletException;
import javax.servlet.ServletInputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

@WebServlet(name = "requestBodyStringServlet", urlPatterns = "/request-body-string")
public class RequestBodyStringServlet extends HttpServlet {

    // httpservlet을 상속받은 클래스에서 service 메소드를 오버라이딩 함에따라서 , request가 들어오면, service 메소드가 작동된다.

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        ServletInputStream inputStream = request.getInputStream(); // 요청으로부터 정보를 얻는다 .

        // http 메시지 바디의 데이터를 inputStream을 사용해서 직접 읽을 수 있다.

        String messageBody = StreamUtils.copyToString(inputStream,
                StandardCharsets.UTF_8);
        // http 메시지의 body 부분을 다음의 코드를 확인한다.
        System.out.println("messageBody = " + messageBody);
        response.getWriter().write("ok");
    }
}
