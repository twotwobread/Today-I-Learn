// file name: lab2_1.java
// 정해진 출력 형태로 출력하는 시스템
// author : Lee suyoung (2022 - 01 - 18)

package lab2;

public class lab2_1 {
    static void printMultTable(int num){
        for(int i = 1; i<=num; i++){
            for(int j=1; j<=i; j++){
                System.out.printf("%d ", i*j);
            }
            System.out.println();
        }
    }

    public static void main(String[] arg){
        printMultTable(7);
    }
}
