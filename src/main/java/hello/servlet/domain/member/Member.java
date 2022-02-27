package hello.servlet.domain.member;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Member {

    private Long id;
    private String username;
    private int age;

    public Member(){

    }

    public Member(String username, int age){
        // id는 저장소에 저장함에 따라 자동 할당된다.
        this.username = username;
        this.age = age;
    }
}
