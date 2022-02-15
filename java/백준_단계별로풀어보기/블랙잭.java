package 단계별로풀어보기.입출력과사칙연산;
/*
N장의 카드 중 3장을 골라야 하는데 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
        M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
        3 <= N <= 100, 10 <= M <= 300,000
        카드에 쓰여 있는 수가 주어지면 이 값은 100,000을 넘지 않는 양의 정수이다.
        합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
*/

// 카드의 개수에 따라 하니까 최대 반복문을 통해서 이 정도가 나오고 1,000,000 + 100
import java.util.*;
public class 블랙잭 {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        // 카드 개수, 기준 숫자 입력
        int n = Integer.parseInt(sc.next());
        int m = Integer.parseInt(sc.next());

        // 카드 정보 입력
        int[] array = new int[n];
        for (int i = 0; i<n; i++){
            array[i] = Integer.parseInt(sc.next());
        }
        int result = -1; // 범위 밖의 수 저장
        for (int i = 0; i< n-2; i++){ // 카드 3장의 더하기 위한 반복문 구성
            for (int j = i+1; j<n-1; j++){
                for (int k = j+1; k<n; k++){
                    int temp = array[i] + array[j] + array[k];
                    if (temp <= m && temp > result)
                        result = temp;
                }
            }
        }
        System.out.print(result);
        return;
    }
}
// 이게 틀렸다고 하는데 그 이유가 뭘까?
// 조건이 M에 가장 가까운 카드 3장의 합이기 때문에 괜찮을꺼 같은데,,,
// k = i+2라고 했는데 사실 이렇게 되면 말이 안됬었다. 겹치는 값을 더하는 경우도 생기고
// k = j+1로 고쳤다.
