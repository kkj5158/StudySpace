package jpabook.jpashop.repository;

import jpabook.jpashop.domain.Member;
import jpabook.jpashop.repository.MemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Rollback;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;


@RunWith(SpringRunner.class)
@SpringBootTest
public class MemberRepositoryTest {

    @Autowired MemberRepository memberRepository;

    @Test
    @Transactional
    //@Rollback(false) // 실제 DB에 test한 결과를 저장하고 insert 쿼리를 보고 싶을때
    //
    public void save_findone_test(){

        //given
        Member member = new Member();
        member.setName("memberA");

        //when
        memberRepository.save(member);

        Member findMember = memberRepository.findone(member.getId());

        // then
        Assertions.assertThat(findMember.getId()).isEqualTo(member.getId());

        Assertions.assertThat(findMember.getName()).isEqualTo(member.getName());

        Assertions.assertThat(findMember).isEqualTo(member);

    }




    @Test
    @Transactional
    //@@Rollback(false)
    public void findAlltest(){


        //given

        List<Member> memberList = new ArrayList<Member>();
        List<Member> findmemberList;

        Member member1 = new Member();
        Member member2 = new Member();
        Member member3 = new Member();


        memberList.add(member1);
        memberList.add(member2);
        memberList.add(member3);


        //when
        memberRepository.save(member1);
        memberRepository.save(member2);
        memberRepository.save(member3);

        findmemberList = memberRepository.findAll();

        Assertions.assertThat(memberList).isEqualTo(findmemberList);





    }


    @Test
    @Transactional
    public void findByName() {


        List<Member> memberList = new ArrayList<Member>();
        List<Member> findmemberList;

        Member member1 = new Member();
        Member member2 = new Member();
        Member member3 = new Member();

        member1.setName("MemberA");
        member2.setName("MemberA");
        member3.setName("MemberA");

        memberList.add(member1);
        memberList.add(member2);
        memberList.add(member3);


        //when
        memberRepository.save(member1);
        memberRepository.save(member2);
        memberRepository.save(member3);

        findmemberList = memberRepository.findByName("MemberA");

        Assertions.assertThat(memberList).isEqualTo(findmemberList);
    }
}

