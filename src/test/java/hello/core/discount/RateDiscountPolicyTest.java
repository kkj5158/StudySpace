package hello.core.discount;

import hello.core.AppConfig;
import hello.core.Order.OrderService;
import hello.core.Order.OrderServiceImpl;
import hello.core.member.Grade;
import hello.core.member.Member;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class RateDiscountPolicyTest {

    //given

    /*
    RateDiscountPolicy policy = new RateDiscountPolicy();
    OrderServiceImpl orderService = new OrderServiceImpl(memberRepository, discountPolicy);
     - > APPCONFIG 로의 전환, ocp와 dp 원칙 지키게끔 .
     */

    DiscountPolicy policy;
    OrderService orderService;

    @BeforeEach
    public void beforeEach() {
        AppConfig appConfig = new AppConfig();
        policy = appConfig.discountPolicy();
        orderService = appConfig.orderService();
    }



    @Test
    @DisplayName("VIP는 10% 할인이 적용되어야 한다.")
    void vip_o (){

        // given
        Member member = new Member(1L, "memberVIP", Grade.VIP);

        //when
        int discount = policy.discount(member, 10000);

        //then
        assertThat(discount).isEqualTo(1000);


    }

    @Test
    @DisplayName("VIP가 아니면 할인이 적용되지 않아야 한다.")
    void vip_x(){

        //given
        Member member = new Member(2L, "memberBASIC", Grade.BASIC);

        //when
        int discount = policy.discount(member, 10000);

        //then
        assertThat(discount).isEqualTo(0);

    }
}