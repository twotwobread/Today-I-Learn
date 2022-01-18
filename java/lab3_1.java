// file name : lab3_1.java
// 10개의 배열값을 입력받은 후 선택정렬을 사용하여 정렬 후 출력
// author : Lee Suyoung ( 2022 - 01 - 18 )
package lab3;
import java.util.Scanner;
public class lab3_1 {
    static void sort_select(int[] array){
        int temp, min, min_value;
        for(int i = 0; i<array.length-1; i++){
            min = i;
            min_value = array[i];
            for(int j = i+1; j<array.length; j++){
                if(min_value>array[j]){
                    min = j;
                    min_value = array[j];
                }
            }
            if(min != i){
                temp = array[min];
                array[min] = array[i];
                array[i] = temp;
            }
        }
    }

    public static void main(String[] arg){
        Scanner in = new Scanner(System.in);
        int[] arr = new int[10];
        System.out.println(arr.length);
        for(int i=0; i<arr.length; i++){
            arr[i] = in.nextInt();
            System.out.println(arr[i]);
        }
        for(int i = 0; i<arr.length; i++){
            System.out.printf("%d ", arr[i]);
        }
        sort_select(arr);
        for(int i = 0; i<arr.length; i++){
            System.out.printf("%d ", arr[i]);
        }
    }
}
