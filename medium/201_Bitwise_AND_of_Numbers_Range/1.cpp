// 단순히 for문 돌면 시간초과난다.
// 그래서, 각 비트별로 계산한다.
// 21억 == 32비트 표현 -> 32번 비교하면 됨.
// 첫번째 비트는 주기가 2임
// 두번째 비트는 주기가 4임
// 주기: 2 -> 4 -> 8 따라서 2^n 주기임. n = 1부터 시작.
// 그래서, left ~ right 사이 거리 구한 후, 초기 left 값 확인 후, 1번째 비트부터 확인한다.
    // 1이면, 차이가 1 이상이면 0
    // 0이면, 그냥 0
// 0인건 신경 안써도 되고, 1일때만 신경쓴다.
// 이전 비트까지 봤을 때 차이가 나머지 비트 다 1 되고 뛰어 넘을 때 내 비트가 0이 된다.
    // 그래서, right - left 값보다 내 비트가 0이 되려면 더해져야 하는 값이 더 작으면 0, 크면 1
// 그래서, result = 0 해놓고, left 뒤에서부터 for문 돌면서 합 누적해가며 상위 비트에서 누적값 뺀 나머지와 차이 비교 
// 비교 결과 누적값이 더 크면 1을 shift 해서 result에 합연산으로 추가.
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int result = 0;

        int diff = right - left;

        int idx = 0;
        int sum = 0;
        int temp = left;
        while (temp > 0) {
            int div = temp % 2;
            temp /= 2;

            if (div != 0) {
                if ((1 << idx) - sum > diff) {
                    break;
                }
                sum += (1 << idx);
            }
            
            idx++;
        }

        return (left >> idx) << idx;
        
    }
};
