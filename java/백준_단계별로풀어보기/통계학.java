package 단계별로풀어보기.입출력과사칙연산;
/*
N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. N은 홀수라고 가정.
1. 산술평균 : N개의 수들의 합을 N으로 나눈 값.
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을때 그 중앙에 위치하는 값.
3. 최반값: 가장 많이 나타난 수.
4. 범위 : N개 수들 중 최댓값과 최솟값의 차이.
 */

import java.util.Scanner;
import java.util.Arrays;
public class 통계학 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        // n 입력
        int n = sc.nextInt();
        // 통계를 위한 변수 초기화
        int sum = 0;
        int[] freq = new int[8001]; // 값의 범위가 -4000~4000이라서
        int[] numArray = new int[n];
        for (int i = 0; i<n; i++){
            int num = sc.nextInt();
            numArray[i] = num;
            sum += num; // 산술 평균을 위함.
            freq[num+4000] += 1; // 빈도를 위함.
        }
        Arrays.sort(numArray);
        System.out.println(Math.round((float)sum/(float)n));
        System.out.println(numArray[n/2]); // 중앙값 넣을 것
        int freqMax = Arrays.stream(freq).max().getAsInt();
        int count = 0, index = 0;
        for (int i = 0; i<freq.length; i++) {
            if (freq[i] == freqMax) {
                count += 1;
                index = i;
            }
            if (count == 2)
                break;
        }
        System.out.println(index-4000);
        System.out.println(numArray[n-1] - numArray[0]);
    }
}
