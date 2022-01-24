// file name : lab10_1.java
// vector를 이용하여 100 - 1000 범위의 난수 생성 후 값을 저장.
// 최소, 최대값을 찾고 출력 후 정렬 출력.
// author : Lee Suyoung(2022-01-24)

package lab10;

import java.lang.*;
import java.util.*;

public class lab10_1 {
    int findMax(Vector<Integer> v){
        int result = v.get(0);
        for(int i = 1; i<v.capacity(); i++){
            if(result < v.get(i))
                result = v.get(i);
        }
        return result;
    }
    public static void main(String[] args){
        lab10_1 l = new lab10_1();
        Vector<Integer> vector = new Vector<Integer>(20);
        Collection<Integer> collection;

        System.out.println("정렬하기 전 벡터 값 출력 : ");
        for(int i = 0; i<vector.capacity(); i++){
            vector.add((int)Math.round(Math.random()*(900-1))+100);
            System.out.print(vector.get(i)+" ");
        }
        System.out.println();

        int max = l.findMax(vector);
        int min = Collections.min(vector);
        Collections.sort(vector);

        System.out.println();
        System.out.println("최소값, 최대값 : "+min+", "+max);
        System.out.println("정렬 후 벡터 값 출력 : ");
        for(int i = 0; i<vector.capacity(); i++){
            System.out.print(vector.get(i)+" ");
        }
    }
}
