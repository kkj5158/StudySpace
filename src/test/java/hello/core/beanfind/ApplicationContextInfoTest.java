package hello.core.beanfind;

import hello.core.AppConfig;
import jdk.jfr.StackTrace;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.config.BeanDefinition;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;



public class ApplicationContextInfoTest {

    // Spring 컨테이너
    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext((AppConfig.class));

    @Test
    @DisplayName("모든 빈 출력하기")
    void findAllBean(){
        String[] beanDefintionNames = ac.getBeanDefinitionNames();
        for(String beanDefinitionName : beanDefintionNames){
            Object bean = ac.getBean(beanDefinitionName);
            System.out.println("name = " + beanDefinitionName + "object = " + bean);
        }
    }

    @Test
    @DisplayName("애플리케이션 빈 출력하기")
    void findAppApplicationBean(){
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();
        for(String beanDefinitionName : beanDefinitionNames){
            BeanDefinition beanDefinition =
                    ac.getBeanDefinition(beanDefinitionName);

            if (beanDefinition.getRole() == BeanDefinition.ROLE_APPLICATION) {
                Object bean = ac.getBean(beanDefinitionName);
                System.out.println("name=" + beanDefinitionName + " object=" +
                        bean);
            }
        }



    }




}
