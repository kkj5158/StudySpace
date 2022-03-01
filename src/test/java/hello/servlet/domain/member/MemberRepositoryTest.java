package hello.servlet.domain.member;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class MemberRepositoryTest {

    MemberRepository memberRepository = MemberRepository.getInstance();


    @AfterEach
    void clear(){
        memberRepository.clearStore();
    }

    @Test
    void save() {
        //given
        Member savemember = new Member("kim", 22);

        //when
        memberRepository.save(savemember);
        Member findmember = memberRepository.findById(savemember.getId());


        //then
        assertThat(findmember).isEqualTo(savemember);
    }


    @Test
    void findById() {
        // given

        // when

        // then
    }



    @Test
    void findAll() {

        //given
        Member member1 = new Member("member1", 20);
        Member member2 = new Member("member2", 30);
        memberRepository.save(member1);
        memberRepository.save(member2);
        //when
        List<Member> result = memberRepository.findAll();
        //then
        assertThat(result.size()).isEqualTo(2);
        assertThat(result).contains(member1, member2);

    }

    @Test
    void clearStore() {
        //given

        //when

        //then
    }
}