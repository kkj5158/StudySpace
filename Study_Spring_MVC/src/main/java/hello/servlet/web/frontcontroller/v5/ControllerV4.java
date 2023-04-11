package hello.servlet.web.frontcontroller.v5;

import java.util.Map;

public interface ControllerV4 {
    String process(Map<String, String> paramMap, Map<String, Object> model);
}