// file name : lab2_3.java
// 올해 1월 1일이 어떤 요일인지 입력 받은 후, 달력을 출력 (단, 2월은 무조건 28일로 가정)
// 빈칸은 *로 채운다.
// author : Lee suyoung ( 2022 - 01 -18 )


package lab2;
import java.lang.reflect.Array;
import java.util.Scanner;
import java.util.Arrays;
public class lab2_3 {
    static void PrintCalendar(String wd){
        String[] weekDay = {"월요일", "화요일", "수요일", "목요일", "금요일", "토요일"};
        int[] monthDay = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int w_num = Arrays.asList(weekDay).indexOf(wd) + 1;
        w_num = (w_num==7)?0:w_num;
        int weekJump = 0;

        for(int i = 1; i<=12; i++){
            System.out.println(i +"월");
            weekJump = 0;
            for(int j = 1; j<=monthDay[i];){
                if (w_num!=0){
                    System.out.print("* ");
                    w_num -= 1;
                    weekJump+=1;
                    continue;
                }
                System.out.printf("%d ", j);
                weekJump += 1;
                j++;
                if (weekJump/7==1) {
                    System.out.println();
                    weekJump = 0;
                }
            }
            w_num = ((7-weekJump)<7)?(7-weekJump):0;
            System.out.println();
        }
    }

    public static void main(String[] arg){
        Scanner in = new Scanner(System.in);
        while(true){
            System.out.print("요일을 입력하시오 : ");
            if(in.hasNext()==false){
                break;
            }
            String str = in.next();
            PrintCalendar(str);
        }
    }
}
