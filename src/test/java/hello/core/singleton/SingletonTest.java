package hello.core.singleton;

import hello.core.AppConfig;
import hello.core.member.MemberService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.sql.SQLOutput;

import static org.assertj.core.api.Assertions.assertThat;

public class SingletonTest {

    @Test
    @DisplayName("스프링 없는 순수한 DI 컨테이너")
    void pureContainer(){

        AppConfig appConfig =new AppConfig();

        //1. 조회 : 호출할 때 마다 객체를 생성

        MemberService memberService1 = appConfig.memberService();

        //2 . 조희 : 호출할때 마다 객체를 생성

        MemberService memberService2 = appConfig.memberService();

        // 참조값이 다른 것을 확인

        System.out.println("memberService 1 = " + memberService1);
        System.out.println("memberService 2 = " + memberService2);

        assertThat(memberService1).isNotSameAs(memberService2);


    }

    @Test
    @DisplayName("싱글톤 패턴을 적용한 객체 사용")
    public void singletonServiceTest(){

        //new SingletonService();
        // private으로 생성자를 막아두었다. 컴파일 오류가 발생하다.

        //1. 조회 : 호출할때 마다 같은 객체를 반환

        SingletonService singletonService1 = SingletonService.getInstance();
        SingletonService singletonService2 = SingletonService.getInstance();

        // 참조값이 동일한지 확인

        System.out.println("singletonService1 = " + singletonService1);
        System.out.println("singletonService2 = " + singletonService2);

        assertThat(singletonService1).isSameAs(singletonService2);

        singletonService1.logic();

    }
}
