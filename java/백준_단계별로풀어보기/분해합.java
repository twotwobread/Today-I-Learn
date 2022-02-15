package 단계별로풀어보기.입출력과사칙연산;

import java.util.Scanner;
public class 분해합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // n 입력

        // 최소 값, 최대 값 찾기
        int intNum = sc.nextInt();
        int minValue = intNum - (Integer.toString(intNum).length() * 9);
        if (minValue < 0)
            minValue = 0;
        int maxValue = intNum;
        // 생성자 찾기
        int result = findConstructor(minValue, maxValue);
        System.out.print(result);
        return;
    }
    public static int findConstructor(int minValue, int maxValue) {
        for (int i = minValue; i < maxValue; i++) {
            int sum = i;
            String[] str = Integer.toString(i).split(""); // 한자리씩 배열에 저장하기 위해서 split("")을 취한 모습.
            for (int j = 0; j < str.length; j++) {
                sum += Integer.parseInt(str[j]);
            }
            if (sum == maxValue)
                return i;
        }
        return 0;
    }
}
// 계속적으로 런타임 에러 (NumberFormat)이 발생했다.
// NumberFormat은 숫자를 문자, 문자를 숫자로 바꾸는 과정에서 발생하는 에러이다.
// 숫자 사이에 문자가 있거나 띄어쓰기가 있거나 수가 자료형을 벗어날 정도로 큰 경우에 발생하는데
// 나의 문제점은 minValue가 음수가 될 수 있다는 문제 때문에 발생을 했고 음수가 되는 경우엔 0으로 처리하여 해결했다.
