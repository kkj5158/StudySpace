package com.shop.repository;

import com.shop.entity.Item;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface ItemRepository extends JpaRepository<Item, Long>{
 // JpaRepository에는 기본적인 CRUD 및 페이징 처리를 위한 메소드가 저장되어있다.

 List<Item> findByItemNm(String itemNm);

 //JPA는 함수이름만으로 함수의 기능(쿼리)를 대신 작성해주는 마법같은 기능이 있다.
 List<Item> findByItemNmOrItemDetail(String itemNm, String itemDetail);

 List<Item> findByPriceLessThan(Integer price);

 List<Item> findByPriceLessThanOrderByPriceDesc(Integer price);

 @Query("select i from Item i where i.itemDetail like " +
         "%:itemDetail% order by i.price desc")
 List<Item> findByItemDetail(@Param("itemDetail") String itemDetail);


}