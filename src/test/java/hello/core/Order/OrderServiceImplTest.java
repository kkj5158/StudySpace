package hello.core.Order;

import hello.core.AppConfig;
import hello.core.member.Grade;
import hello.core.member.Member;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class OrderServiceImplTest {

    //given

    /*

    MemberService memberService = new MemberServiceImpl(memberRepository);
    OrderServiceImpl orderService = new OrderServiceImpl(memberRepository, discountPolicy);
    - > APPCONFIG 로의 전환, ocp와 dp 원칙 지키게끔 .
    */

    MemberService memberService;
    OrderService orderService;

    @BeforeEach
    public void beforeEach() {
        AppConfig appConfig = new AppConfig();
        memberService = appConfig.memberService();
        orderService = appConfig.orderService();
    }



    @Test
    void createOrder() {

        //given
        long memberId = 1L;

        Member member = new Member(memberId, "KJS" , Grade.VIP);


        //when
        memberService.join(member);

        int exdiscountprice = 1000;

        Order order = orderService.createOrder(1L, "apple", 10000);

        //then

        Assertions.assertThat(order.getDiscountPrice()).isEqualTo(1000);
    }
}