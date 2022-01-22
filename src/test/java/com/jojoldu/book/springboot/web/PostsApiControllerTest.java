package com.jojoldu.book.springboot.web;

import com.jojoldu.book.springboot.domain.posts.PostsRepository;
import com.jojoldu.book.springboot.web.dto.PostSaveRequestDto;
import org.junit.After;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.web.server.LocalServerPort;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class PostsApiControllerTest {

    @LocalServerPort
    private int port;

    @Autowired
    private PostsRepository postsRepository;

    @After
    public void tearDown() throws Exception{
        postsRepository.deleteAll();
    }

    @Test
    public void Posts_등록된다() throws Exception {

        String title = "title";
        String content = "content";
        PostSaveRequestDto requestDto = PostSaveRequestDto.builder().title(title).content(content).author("author").build();

        String url = "http://localhost:" + port + "/api/v1/posts";

        ResponseEntity<Long> responseEntity = restTemplate.postForEntity(url, requestDto, Long.class);

        assertThat(responseEntity.getStatusCode()).isEqualTo(HttpStatus.OK);


    }
}
