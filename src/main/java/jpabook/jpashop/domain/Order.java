package jpabook.jpashop.domain;


import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter @Setter
public class Order {

    @Id
    @GeneratedValue
    private Long id;

    @ManyToOne
    private Member member;

    @OneToOne
    private Delivery delivery;







}
