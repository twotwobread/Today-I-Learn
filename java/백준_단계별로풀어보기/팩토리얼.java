package 단계별로풀어보기.입출력과사칙연산;

import java.util.Scanner;

public class 팩토리얼 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] array = new int[13];
        array[0] = 1;
        array[1] = 1;
        // n 입력
        int n = sc.nextInt();
        System.out.println(factorial(n, array));
    }

    static int factorial(int num, int[] array) {
        if (array[num] != 0)
            return array[num];
        array[num] = factorial(num-1, array) * num;
        return array[num];
    }
}
