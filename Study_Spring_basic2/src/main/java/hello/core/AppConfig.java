package hello.core;

import hello.core.Order.OrderService;
import hello.core.Order.OrderServiceImpl;
import hello.core.discount.DiscountPolicy;
import hello.core.discount.FixDiscountPolicy;
import hello.core.discount.RateDiscountPolicy;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import hello.core.member.MemoryMemberRepository;
// 스프링으로의 전환
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/* 객체의 생성과 의존관계 주입을 담당합니다 */

@Configuration
public class AppConfig {

    @Bean
    public MemberService memberService() {

        return new MemberServiceImpl(MemberRepository());
    }

    @Bean
    public MemoryMemberRepository MemberRepository() {

        return new MemoryMemberRepository();
    }

    @Bean
    public OrderService orderService(){

        return new OrderServiceImpl(MemberRepository(), discountPolicy());
    }

    @Bean
    public DiscountPolicy discountPolicy() {
        //return new FixDiscountPolicy(); // APPCONFIG의 구성요소만 변경하면 된다.
        return new RateDiscountPolicy();
    }

    /*
    리팩토링의 장점 -> 역할들이 명확하게 드러나고 있다.
     */


}
