# file name : lab1_2.java
# 3개의 수를 입력받고 삼각형을 만들 수 있는지 판별 후 가능하다면 넓이 계산 후 출력
# author : Lee suyoung ( 2022-01-17 )

package lab1;
import java.lang.Math;
import java.util.Scanner;

public class lab1_2 {
	static double cal_int(Scanner in) {
		double s=0.0, area=0.0;
		System.out.print("삼각형의 각 변의 길이를 입력하시오 : ");
		int num1 = in.nextInt();
		int num2 = in.nextInt();
		int num3 = in.nextInt();
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
	static double cal_str(Scanner in) {
		double s=0.0, area=0.0;
		System.out.print("삼각형의 각 변의 길이를 입력하시오 : ");
		String num_str1 = in.next();
		String num_str2 = in.next();
		String num_str3 = in.next();
		int num1 = Integer.parseInt(num_str1);
		int num2 = Integer.parseInt(num_str2);
		int num3 = Integer.parseInt(num_str3);
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
	
	public static void main(String[] arg) {
		Scanner in = new Scanner(System.in);
		double result = cal_int(in);
		if (result!=-1) {
			System.out.printf("삼각형의 넓이 : %f\n", result);
		}
		double result2 = cal_str(in);
		if (result2!=-1) {
			System.out.printf("삼각형의 넓이 : %f\n", result2);
		}
	}
}
