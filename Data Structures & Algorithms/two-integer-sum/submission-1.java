class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> m = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int c1=target-nums[i];
            if (m.containsKey(c1)){
                return new int[] {m.get(c1),i};
            }
            m.put(nums[i],i);
        }
        return new int[]{};
    }
}
