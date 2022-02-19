

import java.util.Arrays;
public class Solution {
    public static void main(String[] args) throws ArrayIndexOutOfBoundsException {
        String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
        String[] result = solution(record);
        System.out.print(result);
    }
    public static String[] solution(String[] record) {
        String[] answer = new String[record.length];
        String[] uid = new String[record.length];

        for (int i = 0; i< record.length; i++){
            String[] action = record[i].split(" ");

            if (action[0].equals("Enter")){
                if (Arrays.asList(uid).contains(action[1])) {
                    String[] compare = answer[Arrays.asList(uid).indexOf(action[1])].split("님");
                    if (!compare[0].equals(action[2])) {
                        for (int k = 0; k < uid.length; k++) {
                            if (action[1].equals(uid[k])){
                                String[] temp = answer[k].split("님");
                                answer[k] = action[2]+"님"+temp[1];
                            }
                        }
                    }
                }
                String tail = "님이 들어왔습니다.";
                uid[i] = action[1];
                answer[i] = action[2]+tail;
            }
            else if (action[0].equals("Leave")){
                String tail = "님이 나갔습니다.";
                for (int k=0; k< uid.length; k++){
                    if (uid[k].equals(action[1])){
                        String[] temp = answer[k].split("님");
                        answer[i] = temp[0]+tail;
                        break;
                    }
                }
                uid[i] = action[1];
            }
            else if (action[0].equals("Change")) {
                for (int j = 0; j < answer.length; j++) {
                    if (action[1].equals(uid[j])) {
                        String[] temp = answer[j].split("님");
                        answer[j] = action[2] + "님" + temp[1];
                    }
                }
            }
        }

        return answer;
    }
}
