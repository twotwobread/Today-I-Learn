// file name : lab2_2.java
// 입력된 길이만큼의 정해진 형태의 모양으로 별찍기
// author : Lee suyoung ( 2022 - 01 -18 )
package lab2;
import java.util.Scanner;

public class lab2_2 {
    static void PrintStart(int h){
        for(int i = 1; i<=h; i++){
            for(int j=0; j<i; j++){
                System.out.print("*");
            }
            for(int k=(h*2-1)-(i*2); k>=1; k--){
                System.out.print(" ");
            }
            for(int j=0; j<i; j++){
                if((i==h) && (j>=i-1)){
                    System.out.print("");
                }
                else {
                    System.out.print("*");
                }
            }
            System.out.println();
        }
    }
    public static void main(String[] arg){
        Scanner in = new Scanner(System.in);
        int height;
        while(in.hasNext()){
            height = in.nextInt(); // 높이 입력부분
            System.out.println("높이 : "+ height);
            PrintStart(height);
        }
    }
}
