//file name : searchPrimeNumber.java
// 스레드 10개를 돌려서 하나의 Vector를 공유변수로 가지고 겹치지 않는 10000개의 소수를 찾는다.
// author : Lee Suyoung ( 2022-01-25 )

import java.io.IOException;
import java.lang.*;
import java.util.ArrayList;
import java.util.Vector;

public class test {
    class ThreadPrimeNumber extends Thread{
        public static Vector<Integer> primeArray = new Vector<Integer>();
        String name;

        ThreadPrimeNumber(){ this(""); }
        ThreadPrimeNumber(String name){ this.name = name; }

        public String toString(){
            String result="";
            for(int i=0; i<primeArray.size(); i++) {
                result += primeArray.get(i) + " ";
                if((i+1)%10==0)
                    result+="\n";
            }
            return result;
        }
        @Override
        public void run() {
            int num = 2;

            while(true) {
                boolean primeCheck = true;
                synchronized (this) { // critical section
                    if (primeArray.size() >= 10000) { // 쓰레드 종류 조건문
                        System.out.println(name + "번째 스레드가 길이를 만족하여 종료되었습니다.");
                        break;
                    }
                }
                if (num > 2) { // 소수 찾는 부분
                    for (int i = 2; i < num; i++) {
                        if (num % i == 0) {
                            primeCheck = false;
                            break;
                        }
                    }
                }
                if (primeCheck == true) { // 소수인 경우
                    synchronized (this) { // critical section
                        if (primeArray.size() <= 0) { // 공유변수 배열이 비어있는 경우 즉 2인 경우라서 값을 add
                            primeArray.add(num);
                        } else { // 2이상인 경우
                            if ((num > primeArray.get(primeArray.size() - 1))) { // 찾은 소수가 배열안에 없는 경우
                                primeArray.add(num);
                            }
                        }
                    }
                }
                num++;
            }
        }
    }
    public static void main(String[] argv) {
        ThreadPrimeNumber th1, th2, th3, th4, th5, th6, th7, th8, th9, th10;
        try{
            test t = new test();
            th1 = t.new ThreadPrimeNumber("1");
            th2 = t.new ThreadPrimeNumber("2");
            th3 = t.new ThreadPrimeNumber("3");
            th4 = t.new ThreadPrimeNumber("4");
            th5 = t.new ThreadPrimeNumber("5");
            th6 = t.new ThreadPrimeNumber("6");
            th7 = t.new ThreadPrimeNumber("7");
            th8 = t.new ThreadPrimeNumber("8");
            th9 = t.new ThreadPrimeNumber("9");
            th10 = t.new ThreadPrimeNumber("10");
            th1.start(); th2.start(); th3.start(); th4.start(); th5.start();
            th6.start(); th7.start(); th8.start(); th9.start(); th10.start();
            th1.join(); th2.join(); th3.join(); th4.join(); th5.join();
            th6.join(); th7.join(); th8.join(); th9.join(); th10.join();
            System.out.println(th1);
        } catch (InterruptedException e){
            System.out.println("Generate InterruptedException!!!!!!");
        }
    }
}

// 소수 저장 시 똑같은 수가 삽입되는 경우 발생
// 싱크로나이즈로 크리티컬 섹션을 관리했는데 이유를 찾아봐야할 것 같음.
