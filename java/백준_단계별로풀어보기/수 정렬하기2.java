// nlogn 이어야 해서 한번 라이브러리에 있는 sort 이용해봄
import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] array = new int[n];
        for (int i = 0; i<n; i++){
            array[i] = sc.nextInt();
        }
        
        Arrays.sort(array);
        for (int i = 0; i<n; i++){
            System.out.println(array[i]);
        }
    }
}
