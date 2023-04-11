package hello.servlet.basic.HelloData;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class HelloData {

    private String username;
    private int age;
}

/* lombok이 제공하는 @Getter @Setter 덕분에 다음 겟터와 셋터가 자동으로 추가된다, " */