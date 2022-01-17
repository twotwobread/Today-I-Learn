# file name : lab1_1.java
# 소문자 -> 대문자, 대문자 -> 소문자 , 둘다 아닐 경우 경고 문자 출력
# autor: Lee suyoung (2022-01-17)

package lab1;
import java.util.Scanner;
public class lab1_1 {
	public static void main(String[] arg) {
		Scanner in = new Scanner(System.in);
		while(true) {
			System.out.println("알파벳을 입력하시오 : ");
			if (in.hasNext()==false) {
				break;
			}
			char num = in.next().charAt(0);
			int ialpa = (int)num;
			if ((97<=ialpa)&&(ialpa<=122)){
				ialpa -= 32;
				System.out.println((char)ialpa);
			}
			else if ((65<=ialpa)&&(ialpa<=90)){
				ialpa += 32;
				System.out.println((char)ialpa);
			}
			else {
				System.out.println("알파벳이 아닙니다!!!!!");
			}
		}
	}
}
