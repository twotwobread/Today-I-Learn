// file name : lab3_2.java
// 로또 번호 자동 생성기 : 매주 창협이는 5개의 복권을 삽니다.
// 하나의 set 안에서 중복된 숫자는 없어야하고 5x6의 2차원 배열을 생성합니다. 다섯 개의 각 행에 속한 6개의 숫자가 1 set의 로또 번호를 의미하며,
// 각 숫자는 1~45 사이의 랜덤 번호입니다. 각 로또 set을 정렬하여 재저장합니다. 5 set의 로또 번호를 출력합니다.
// author : Lee Suyoung( 2022 - 01 - 18 )

package lab3;
import java.lang.Math;
public class lab3_2 {
    public static void main(String[] arg){
        int[][] array = new int[5][6];
        int i = 0;
        int row = 0;
        boolean check = true;
        while(i < array.length){
            int random = (int)(Math.random() * (45-1+1)+1);
            for(int j = 0; j<array[i].length; j++){ // 배열안에 존재하는지 확인
                if (array[i][j] == random) {
                    check = false;
                    break;
                }
            }
            if (check==true){
                array[i][row] = random;
                row++;
            }
            if (row==6) {
                i++;
                row=0;
            }
        }
        for(int k=0; k<array.length; k++){
            System.out.println((k+1)+"번째 로또 번호 : ");
            for(int j = 0; j<array[k].length; j++){
                System.out.printf("%d ", array[k][j]);
            }
            System.out.println();
        }
    }
}
