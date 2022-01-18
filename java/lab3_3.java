// file name : lab3_3.java
// 3개의 정수를 쉼표와 공백으로 구분하여 한 줄에 입력 시, 삼각형을 만들 수 있는 지 판별 후
// 가능하다면 삼각형의 넓이를 계산하시오.
// author : Lee Suyoung( 2022 - 01 - 18 )
package lab3;

import java.util.Scanner;

public class lab3_3 {
    static double calculate(int num1, int num2, int num3){
        double s=0.0, area=0.0;
        if(((num1+num2)>num3)||((num2+num3)>num1)||((num3+num1)>num2)){
            s = (num1+num2+num3)/2;
            area = Math.sqrt(s*(s-num1)*(s-num2)*(s-num3));
        }
        else {
            System.out.println("잘못된 입력값입니다.");
            return -1;
        }
        return area;
    }
    public static void main(String[] arg){
        System.out.print("삼각형의 각 변의 길이를 입력하시오 : ");
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        String[] str_arr = new String[3];
        str_arr = str.split(",");
        int a = Integer.parseInt(str_arr[0].trim());
        int b = Integer.parseInt(str_arr[1].trim());
        int c = Integer.parseInt(str_arr[2].trim());
        double result = calculate(a, b, c);
        if (result != -1) {
            System.out.printf("삼각형의 넓이는 %f입니다.\n", result);
        }
    }
}
