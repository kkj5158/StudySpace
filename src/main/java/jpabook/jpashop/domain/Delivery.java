package jpabook.jpashop.domain;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;


@Entity
@Getter @Setter
public class Delivery {

    @Id
    @GeneratedValue
    private Long id;

    @OneToOne
    private Order order;

    @Embedded
    private Address address;

    private DeliveryStauts stauts;
}
